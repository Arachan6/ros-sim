cmake_minimum_required(VERSION 3.8)
project(brazo_robotico)

# Find dependencies
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find ROS 2 packages
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)  # For ROS 2 core functionality, optional if no nodes
find_package(xacro REQUIRED)   # For processing xacro files

# Install directories (URDF, launch, etc.)
install(
  DIRECTORY urdf launch
  DESTINATION share/${PROJECT_NAME}/
)

# Export package for ROS 2
ament_package()
