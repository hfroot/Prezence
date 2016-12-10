# %Tag(FULLTEXT)%
cmake_minimum_required(VERSION 2.8.3)
project(head_pose_monitor)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS geometry_msgs roscpp rospy)

## Declare a catkin package
catkin_package(
  CATKIN_DEPENDS
    geometry_msgs roscpp rospy
)

## Build talker and listener
include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(head_pose_monitor src/head_pose_monitor.cpp)

add_dependencies(head_pose_monitor head_pose_monitor_generate_messages_cpp)

target_link_libraries(head_pose_monitor ${catkin_LIBRARIES})

# %EndTag(FULLTEXT)%

