#include "ros/ros.h"
#include "geometry_msgs/PoseArray.h"
#include <iostream>
#include <fstream>
#include <tf/transform_broadcaster.h>
#include <string.h>

void PoseCallback(const geometry_msgs::PoseArray::ConstPtr& msg){
  //double x = msg->poses[0].position.x;
  //double y = msg->poses[0].position.y;
  double roll, pitch, yaw;	

tf::Quaternion q(msg->poses[0].orientation.x, msg->poses[0].orientation.y, msg->poses[0].orientation.z, msg->poses[0].orientation.w);

tf::Matrix3x3 rotMat(q);

rotMat.getRPY(roll,pitch,yaw);

yaw = (-yaw * 180.0 / M_PI) - 90; // conversion to degrees
if( yaw < 0 ) yaw += 360.0; // convert negative to positive angles

pitch = (-pitch * 180.0 / M_PI) - 270; // conversion to degrees
if( pitch < 0 ) pitch += 360.0; // convert negative to positive angles

std::string head_direction;

if(pitch < 70){//left
  if(yaw < 70){//down
    head_direction = "downleft";
  }
  if(yaw >= 70 && yaw <= 110){//horizon
    head_direction = "down";
  }
  if(yaw > 110){//up
    head_direction = "downright";
  }
}

if(pitch >= 70 && pitch <= 110){//middle
  if(yaw < 70){//down
    head_direction = "left";
  }
  if(yaw >= 70 && yaw <= 110){//horizon
    head_direction = "center";
  }
  if(yaw > 110){//up
    head_direction = "right";
  }
}

if(pitch > 110){//right
  if(yaw < 70){//down
    head_direction = "upleft";
  }
  if(yaw >= 70 && yaw <= 110){//horizon
    head_direction = "up";
  }
  if(yaw > 110){//up
    head_direction = "upright";
  }
}



  std::ofstream myfile("Desktop/example.txt", std::ios_base::app);
  myfile << head_direction << std::endl;
  myfile.close();

  ROS_INFO("yaw: %f, y: %f", yaw, pitch);
}

int main(int argc, char** argv){
//clear file first
  /*std::ofstream ofs;
  ofs.open("Desktop/example.txt", std::ofstream::out | std::ofstream::trunc);
  ofs.close();*/


  ros::init(argc, argv, "head_pose_monitor");
  ros::NodeHandle nh;
  ros::Subscriber sub = nh.subscribe("head_pose", 10, PoseCallback);
  ros::spin();
  return 0;
}
