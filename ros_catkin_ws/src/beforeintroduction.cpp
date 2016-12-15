#include "ros/ros.h"
#include "geometry_msgs/PoseArray.h"
#include "skeleton_markers/Skeleton.h"
#include <iostream>
#include <fstream>
#include <tf/transform_broadcaster.h>
#include <string.h>
#include <time.h>
#include <sstream>
#include <string>
#include <cstring>

bool has_started = false;
int slow_writes = 0;

void PoseCallback(const skeleton_markers::Skeleton::ConstPtr& msg){

//get RPY of head
  double roll, pitch, yaw;
  tf::Quaternion q(msg->orientation[0].x, msg->orientation[0].y, msg->orientation[0].z, msg->orientation[0].w);
  tf::Matrix3x3 rotMat(q);
  rotMat.getRPY(pitch,yaw,roll);

  yaw = (-yaw * 180.0 / M_PI) + 90; // conversion to degrees
  if( yaw < 0 ) yaw += 360.0; // convert negative to positive angles

  pitch = (pitch * 180.0 / M_PI) - 270; // conversion to degrees
  if( pitch < 0 ) pitch += 360.0; // convert negative to positive angles

//categorise head_direction based on yaw/pitch
  std::string head_direction;

  if(pitch < 85){//down
    if(yaw < 70){//left
      head_direction = "downleft";
    }
    if(yaw >= 70 && yaw <= 110){//middle
      head_direction = "down";
    }
    if(yaw > 110){//right
      head_direction = "downright";
    }
  }

  if(pitch >= 85 && pitch <= 95){//horizon
    if(yaw < 70){//left
      head_direction = "left";
    }
    if(yaw >= 70 && yaw <= 110){//middle
      head_direction = "center";
    }
    if(yaw > 110){//right
      head_direction = "right";
    }
  }

  if(pitch > 95){//up
    if(yaw < 70){//left
      head_direction = "upleft";
    }
    if(yaw >= 70 && yaw <= 110){//middle
      head_direction = "up";
    }
    if(yaw > 110){//right
      head_direction = "upright";
    }
  }

/* -------
['0 head', '1 neck', '2 torso', '3 left_shoulder', '4 left_elbow', '5 left_hand', '6 right_shoulder', '7 right_elbow', '8 right_hand', '9 left_hip', '10 left_knee', '11 left_foot', '12 right_hip', '13 right_knee', '14 right_foot']
------- */


/* -------
facing away, folded arms, gesticulating, moving, covering mouth, hands in pockets, shifting weight
------- */

  tf::Vector3 head;             head.setValue(msg->position[0].x*100, msg->position[0].y*100, msg->position[0].z*100);
  tf::Vector3 neck;             neck.setValue(msg->position[1].x*100, msg->position[1].y*100, msg->position[1].z*100);
  tf::Vector3 torso;           torso.setValue(msg->position[2].x*100, msg->position[2].y*100, msg->position[2].z*100);
  tf::Vector3 l_shoulder; l_shoulder.setValue(msg->position[3].x*100, msg->position[3].y*100, msg->position[3].z*100);
  tf::Vector3 l_elbow;       l_elbow.setValue(msg->position[4].x*100, msg->position[4].y*100, msg->position[4].z*100);
  tf::Vector3 l_hand;         l_hand.setValue(msg->position[5].x*100, msg->position[5].y*100, msg->position[5].z*100);
  tf::Vector3 r_shoulder; r_shoulder.setValue(msg->position[6].x*100, msg->position[6].y*100, msg->position[6].z*100);
  tf::Vector3 r_elbow;       r_elbow.setValue(msg->position[7].x*100, msg->position[7].y*100, msg->position[7].z*100);
  tf::Vector3 r_hand;         r_hand.setValue(msg->position[8].x*100, msg->position[8].y*100, msg->position[8].z*100);
  tf::Vector3 l_hip;           l_hip.setValue(msg->position[9].x*100, msg->position[9].y*100, msg->position[9].z*100);
  tf::Vector3 l_knee;        l_knee.setValue(msg->position[10].x*100, msg->position[10].y*100, msg->position[10].z*100);
  tf::Vector3 l_foot;        l_foot.setValue(msg->position[11].x*100, msg->position[11].y*100, msg->position[11].z*100);
  tf::Vector3 r_hip;          r_hip.setValue(msg->position[12].x*100, msg->position[12].y*100, msg->position[12].z*100);
  tf::Vector3 r_knee;        r_knee.setValue(msg->position[13].x*100, msg->position[13].y*100, msg->position[13].z*100);
  tf::Vector3 r_foot;        r_foot.setValue(msg->position[14].x*100, msg->position[14].y*100, msg->position[14].z*100);

//gesture checks
  std::string gesture;
  gesture = "none";

//poor_posture

  int pTh = 4;
  if( ((head.getZ() < l_shoulder.getZ()) && (head.getZ() < r_shoulder.getZ())) && ((l_shoulder.getZ() < l_hip.getZ()-pTh) && (r_shoulder.getZ() < r_hip.getZ()-pTh)) &&
      (l_hand.getY() < l_shoulder.getY()) && (r_hand.getY() < r_shoulder.getY()) )
  {
    gesture = "poor_posture";
  }


//folded_arms
  if(l_hand.getX() > r_hand.getX()){
    gesture = "folding_arms";
  }

//covering_mouth (hands near face)
  int cmTh = 10;
  if( ((neck.getY() < l_hand.getY()) && (l_hand.getY() < neck.getY()+cmTh+20)) && ((neck.getX()-cmTh < -l_hand.getX()) && (-l_hand.getX() < neck.getX()+cmTh)) ||
      ((neck.getY() < r_hand.getY()) && (r_hand.getY() < neck.getY()+cmTh+20)) && ((neck.getX()-cmTh <  r_hand.getX()) && ( r_hand.getX() < neck.getX()+cmTh)) )
  {
    gesture = "covering_mouth";
  }

//facing away
  if(l_shoulder.getX() > r_shoulder.getX()){
    gesture = "turning_away";
  }

//looking_down
  if(pitch < 75){
    gesture = "looking_down";
  }

//start
  //if((l_hand.getY() > l_shoulder.getY()) && (r_hand.getY() > r_shoulder.getY())
//&& (l_hand.getX() < l_elbow.getX()+6) && (l_hand.getX() > l_elbow.getX()-6)
//&& (r_hand.getX() < r_elbow.getX()+6) && (r_hand.getX() > r_elbow.getX()-6)
//){
  if(r_hand.getY() > r_shoulder.getY()+15){
    //gesture = "start";
    if(!has_started){
      //write start to sync.txt
      std::ofstream startfile("../Prezence/output/sync.txt", std::ios_base::app);
      startfile << "start";
      startfile.close();
    }
    has_started = true;
  }

  if((l_hand.getY() > l_shoulder.getY()-5) && (l_hand.getZ() < l_shoulder.getZ() - 40)){
    gesture = "end";
    if(has_started){
      //write start to sync.txt
      std::ofstream endfile("../Prezence/output/sync.txt", std::ios_base::app);
      endfile << "\nstop\n";
      endfile.close();
    }
  }
//l_hip.getX(), l_hip.getY(), l_hand.getX(), l_hand.getY(), head.getY(), r_hip.getX(), r_hand.getX(), r_hand.getY());
  if(((-l_hand.getX() > -l_hip.getX()+30)&&(l_hand.getY() < l_hip.getY()+5)) && ((r_hand.getY() > head.getY()+15)&&(r_hand.getX() > r_hip.getX()+20))){
    gesture = "##########################";
    if(has_started){
      //write start to sync.txt
      std::ofstream gangnam_file("../Prezence/output/gangnam_file.txt", std::ios_base::app);
      gangnam_file << "opp\n";
      gangnam_file.close();
    }
  }

//get timestamp
  time_t seconds_past_epoch = time(0);

slow_writes++;

if(has_started && (slow_writes%60==0)){
  ROS_INFO("writing_to_file");

//write pitch to head_gaze.txt
  std::ofstream headfile("../Prezence/output/head_gaze.txt", std::ios_base::app);
  headfile << seconds_past_epoch << " " << pitch << std::endl;
  headfile.close();

//write gesture to gesture.txt
  std::ofstream gesturefile("../Prezence/output/gesture.txt", std::ios_base::app);
  gesturefile << seconds_past_epoch << " " << gesture << std::endl;
  gesturefile.close();
}

//check sync for end
  std::string endstring;
  std::ifstream endfile("../Prezence/output/sync.txt");
//for some reason I have to open it twice
  endfile.open("../Prezence/output/sync.txt");
  endfile.close();

  endfile.open("../Prezence/output/sync.txt");
  endfile >> endstring;
  endfile >> endstring;
  endfile.close();
  if(endstring=="stop"){exit(0);}
  ROS_INFO("status: %s", endstring.c_str());

//prints and sleep
  ROS_INFO("position: %f, %f", l_hand.getZ(), l_shoulder.getZ());
  ROS_INFO("gesture: %s", gesture.c_str());
  if(has_started){
    ros::Duration(0).sleep();
  }

}


int main(int argc, char** argv){
//clear file first
  std::ofstream ofs;
  ofs.open("../Prezence/output/head_gaze.txt", std::ofstream::out | std::ofstream::trunc);
  ofs.close();
//clear file first
  std::ofstream ofsg;
  ofsg.open("../Prezence/output/gesture.txt", std::ofstream::out | std::ofstream::trunc);
  ofsg.close();
//clear file first
  std::ofstream ofssy;
  ofssy.open("../Prezence/output/sync.txt", std::ofstream::out | std::ofstream::trunc);
  ofssy.close();
//clear file first
  std::ofstream ofopp;
  ofopp.open("../Prezence/output/gangnam_file.txt", std::ofstream::out | std::ofstream::trunc);
  ofopp.close();

//init ros and create nodehandle
  ros::init(argc, argv, "skeleton_monitor");
  ros::NodeHandle nh;


/*
//check sync for start
  std::string startstring;
  std::ifstream syncfile("../Prezence/output/sync.txt");
//look for start then sleep for a bit
    while(startstring.empty()){
        syncfile.open("../Prezence/output/sync.txt");
        syncfile >> startstring;
        syncfile.close();
        ROS_INFO("Waiting for start, found: %s", startstring.c_str());
        ros::Duration(1).sleep();
    }
   */
 
//declare subscriber to skeleton topic
  ros::Subscriber sub = nh.subscribe("skeleton", 10, PoseCallback);




  ros::spin();
  return 0;
}

