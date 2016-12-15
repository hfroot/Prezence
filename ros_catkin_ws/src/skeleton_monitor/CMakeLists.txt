# %Tag(FULLTEXT)%
cmake_minimum_required(VERSION 2.8.3)
project(skeleton_monitor)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS skeleton_markers roscpp rospy)

## Declare a catkin package
catkin_package(
  CATKIN_DEPENDS
    skeleton_markers roscpp rospy
)

## Build talker and listener
include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(skeleton_monitor src/skeleton_monitor.cpp)

add_dependencies(skeleton_monitor skeleton_monitor_generate_messages_cpp)

target_link_libraries(skeleton_monitor ${catkin_LIBRARIES})

# %EndTag(FULLTEXT)%

