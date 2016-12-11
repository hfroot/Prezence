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

void PoseCallback(const skeleton_markers::Skeleton::ConstPtr& msg){
  
  double roll, pitch, yaw;	

  tf::Quaternion q(msg->orientation[0].x, msg->orientation[0].y, msg->orientation[0].z, msg->orientation[0].w);

  tf::Matrix3x3 rotMat(q);

  rotMat.getRPY(pitch,yaw,roll);

yaw = (-yaw * 180.0 / M_PI) + 90; // conversion to degrees
if( yaw < 0 ) yaw += 360.0; // convert negative to positive angles

pitch = (pitch * 180.0 / M_PI) - 270; // conversion to degrees
if( pitch < 0 ) pitch += 360.0; // convert negative to positive angles

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

  //ROS_INFO("head_direction: %s, yaw: %f, pitch: %f", head_direction.c_str(), yaw, pitch);


/* -------
['0 head', '1 neck', '2 torso', '3 left_shoulder', '4 left_elbow', '5 left_hand', '6 right_shoulder', '7 right_elbow', '8 right_hand', '9 left_hip', '10 left_knee', '11 left_foot', '12 right_hip', '13 right_knee', '14 right_foot']
------- */


/* -------
facing away, folded arms, gesticulating, moving, covering mouth, hands in pockets, shifting weight
------- */

  tf::Vector3 head; head.setValue(msg->position[0].x*100, msg->position[0].y*100, msg->position[0].z*100);
  tf::Vector3 neck; neck.setValue(msg->position[1].x*100, msg->position[1].y*100, msg->position[1].z*100);
  tf::Vector3 torso; torso.setValue(msg->position[2].x*100, msg->position[2].y*100, msg->position[2].z*100);
  tf::Vector3 l_shoulder; l_shoulder.setValue(msg->position[3].x*100, msg->position[3].y*100, msg->position[3].z*100);
  tf::Vector3 l_elbow; l_elbow.setValue(msg->position[4].x*100, msg->position[4].y*100, msg->position[4].z*100);
  tf::Vector3 l_hand; l_hand.setValue(msg->position[5].x*100, msg->position[5].y*100, msg->position[5].z*100);
  tf::Vector3 r_shoulder; r_shoulder.setValue(msg->position[6].x*100, msg->position[6].y*100, msg->position[6].z*100);
  tf::Vector3 r_elbow; r_elbow.setValue(msg->position[7].x*100, msg->position[7].y*100, msg->position[7].z*100);
  tf::Vector3 r_hand; r_hand.setValue(msg->position[8].x*100, msg->position[8].y*100, msg->position[8].z*100);
  tf::Vector3 l_hip; l_hip.setValue(msg->position[9].x*100, msg->position[9].y*100, msg->position[9].z*100);
  tf::Vector3 l_knee; l_knee.setValue(msg->position[10].x*100, msg->position[10].y*100, msg->position[10].z*100);
  tf::Vector3 l_foot; l_foot.setValue(msg->position[11].x*100, msg->position[11].y*100, msg->position[11].z*100);
  tf::Vector3 r_hip; r_hip.setValue(msg->position[12].x*100, msg->position[12].y*100, msg->position[12].z*100);
  tf::Vector3 r_knee; r_knee.setValue(msg->position[13].x*100, msg->position[13].y*100, msg->position[13].z*100);
  tf::Vector3 r_foot; r_foot.setValue(msg->position[14].x*100, msg->position[14].y*100, msg->position[14].z*100);

//gesture checks

  std::string gesture;
  gesture = "none";

//folded_arms
  if(l_hand.getX() > r_hand.getX()){
    gesture = "folded_arms";
  }

//covering_mouth (hands near face)
  int cmTh = 10;
  if( ((neck.getY() < l_hand.getY()) && (l_hand.getY() < neck.getY()+cmTh+10)) && ((neck.getX()-cmTh < -l_hand.getX()) && (-l_hand.getX() < neck.getX()+cmTh)) ||
      ((neck.getY() < r_hand.getY()) && (r_hand.getY() < neck.getY()+cmTh+10)) && ((neck.getX()-cmTh <  r_hand.getX()) && ( r_hand.getX() < neck.getX()+cmTh)) )
  {
    gesture = "covering_mouth";
  }

//hands by side
  //int pkTh = 10;
  //if( ((l_hip.getY()-pkTh-20 < l_hand.getY()) && (l_hand.getY() < l_hip.getY()+pkTh-10)) && ((l_hip.getX()-pkTh < -l_hand.getX()) && (-l_hand.getX() < l_hip.getX()+pkTh)) ||
  //    ((r_hip.getY()-pkTh-20 < r_hand.getY()) && (r_hand.getY() < r_hip.getY()+pkTh-10)) && ((r_hip.getX()-pkTh <  r_hand.getX()) && ( r_hand.getX() < r_hip.getX()+pkTh)) )
  //{
  //  gesture = "hands_by_side";
  //}

//facing away
  if(l_shoulder.getX() > r_shoulder.getX()){
    gesture = "turning_away";
  }

//facing away
  if((l_hand.getY() > l_shoulder.getY()) && (r_hand.getY() > r_shoulder.getY())){
    gesture = "start";
  }


  if(pitch < 75){
    gesture = "looking_down";
  }

  
  time_t seconds_past_epoch = time(0);

  ros::Duration(0).sleep();

  std::ofstream myfile("Prezence/output/head_gaze.txt", std::ios_base::app);
  myfile << seconds_past_epoch << " " << pitch << std::endl;
  myfile.close();

  ROS_INFO("head_position: %f, %f, %f", neck.getX(), -l_hand.getX(), l_hand.getY());
  ROS_INFO("gesture: %s", gesture.c_str());

}

int main(int argc, char** argv){
//clear file first
  std::ofstream ofs;
  ofs.open("Prezence/output/head_gaze.txt", std::ofstream::out | std::ofstream::trunc);
  ofs.close();




  ros::init(argc, argv, "skeleton_monitor");
  ros::NodeHandle nh;

//check sync for start
  std::string value;
std::ifstream syncfile("../Prezence/output/sync.txt");

    while(value.empty()){
        syncfile.close();
        ros::Duration(1).sleep();
        syncfile.open("../Prezence/output/sync.txt");
    syncfile >> value;
    ROS_INFO("value %s", value.c_str());
    }
    ROS_INFO("value %s", value.c_str());
    syncfile.close();



  ros::Subscriber sub = nh.subscribe("skeleton", 10, PoseCallback);
  ros::spin();
  return 0;
}

