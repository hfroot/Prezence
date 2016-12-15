# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "skeleton_markers: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iskeleton_markers:/home/human/ros_catkin_ws/src/skeleton_markers/msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(skeleton_markers_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/human/ros_catkin_ws/src/skeleton_markers/msg/Skeleton.msg" NAME_WE)
add_custom_target(_skeleton_markers_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "skeleton_markers" "/home/human/ros_catkin_ws/src/skeleton_markers/msg/Skeleton.msg" "geometry_msgs/Quaternion:std_msgs/Header:geometry_msgs/Vector3"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(skeleton_markers
  "/home/human/ros_catkin_ws/src/skeleton_markers/msg/Skeleton.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/skeleton_markers
)

### Generating Services

### Generating Module File
_generate_module_cpp(skeleton_markers
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/skeleton_markers
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(skeleton_markers_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(skeleton_markers_generate_messages skeleton_markers_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/human/ros_catkin_ws/src/skeleton_markers/msg/Skeleton.msg" NAME_WE)
add_dependencies(skeleton_markers_generate_messages_cpp _skeleton_markers_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(skeleton_markers_gencpp)
add_dependencies(skeleton_markers_gencpp skeleton_markers_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS skeleton_markers_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(skeleton_markers
  "/home/human/ros_catkin_ws/src/skeleton_markers/msg/Skeleton.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/skeleton_markers
)

### Generating Services

### Generating Module File
_generate_module_eus(skeleton_markers
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/skeleton_markers
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(skeleton_markers_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(skeleton_markers_generate_messages skeleton_markers_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/human/ros_catkin_ws/src/skeleton_markers/msg/Skeleton.msg" NAME_WE)
add_dependencies(skeleton_markers_generate_messages_eus _skeleton_markers_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(skeleton_markers_geneus)
add_dependencies(skeleton_markers_geneus skeleton_markers_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS skeleton_markers_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(skeleton_markers
  "/home/human/ros_catkin_ws/src/skeleton_markers/msg/Skeleton.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/skeleton_markers
)

### Generating Services

### Generating Module File
_generate_module_lisp(skeleton_markers
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/skeleton_markers
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(skeleton_markers_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(skeleton_markers_generate_messages skeleton_markers_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/human/ros_catkin_ws/src/skeleton_markers/msg/Skeleton.msg" NAME_WE)
add_dependencies(skeleton_markers_generate_messages_lisp _skeleton_markers_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(skeleton_markers_genlisp)
add_dependencies(skeleton_markers_genlisp skeleton_markers_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS skeleton_markers_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(skeleton_markers
  "/home/human/ros_catkin_ws/src/skeleton_markers/msg/Skeleton.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/skeleton_markers
)

### Generating Services

### Generating Module File
_generate_module_nodejs(skeleton_markers
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/skeleton_markers
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(skeleton_markers_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(skeleton_markers_generate_messages skeleton_markers_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/human/ros_catkin_ws/src/skeleton_markers/msg/Skeleton.msg" NAME_WE)
add_dependencies(skeleton_markers_generate_messages_nodejs _skeleton_markers_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(skeleton_markers_gennodejs)
add_dependencies(skeleton_markers_gennodejs skeleton_markers_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS skeleton_markers_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(skeleton_markers
  "/home/human/ros_catkin_ws/src/skeleton_markers/msg/Skeleton.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/skeleton_markers
)

### Generating Services

### Generating Module File
_generate_module_py(skeleton_markers
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/skeleton_markers
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(skeleton_markers_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(skeleton_markers_generate_messages skeleton_markers_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/human/ros_catkin_ws/src/skeleton_markers/msg/Skeleton.msg" NAME_WE)
add_dependencies(skeleton_markers_generate_messages_py _skeleton_markers_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(skeleton_markers_genpy)
add_dependencies(skeleton_markers_genpy skeleton_markers_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS skeleton_markers_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/skeleton_markers)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/skeleton_markers
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(skeleton_markers_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(skeleton_markers_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/skeleton_markers)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/skeleton_markers
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(skeleton_markers_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(skeleton_markers_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/skeleton_markers)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/skeleton_markers
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(skeleton_markers_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(skeleton_markers_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/skeleton_markers)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/skeleton_markers
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(skeleton_markers_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(skeleton_markers_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/skeleton_markers)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/skeleton_markers\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/skeleton_markers
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(skeleton_markers_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(skeleton_markers_generate_messages_py std_msgs_generate_messages_py)
endif()
