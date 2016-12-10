#include "ros/ros.h"
#include "geometry_msgs/PoseArray.h"
#include "skeleton_markers/Skeleton.h"
#include <iostream>
#include <fstream>
#include <tf/transform_broadcaster.h>
#include <string.h>

void PoseCallback(const skeleton_markers::Skeleton::ConstPtr& msg){
  double x = msg->position[0].x;
  double y = msg->position[0].y;

  //std::ofstream myfile("Desktop/example2.txt", std::ios_base::app);
  //myfile << head_direction << std::endl;
  //myfile.close();

  ROS_INFO("x: %f, y: %f", x, y);
}

int main(int argc, char** argv){
//clear file first
  /*std::ofstream ofs;
  ofs.open("Desktop/example.txt", std::ofstream::out | std::ofstream::trunc);
  ofs.close();*/


  ros::init(argc, argv, "skeleton_monitor");
  ros::NodeHandle nh;
  ros::Subscriber sub = nh.subscribe("skeleton", 10, PoseCallback);
  ros::spin();
  return 0;
}
