from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg = get_package_share_directory('brazo_robotico')
    print(pkg)
    xacro_file = os.path.join(pkg, 'urdf', 'brazo.urdf.xacro')
    world_file = os.path.join(pkg, 'world', 'escenario.sdf')

    # Comando que convierte xacro a URDF en línea
    robot_description = {'robot_description': Command(['xacro', xacro_file])}

    return LaunchDescription([
        # Lanzar Ignition Gazebo con el mundo
        ExecuteProcess(
            cmd=['ros2', 'launch', 'ros_gz_sim', 'gz_sim.launch.py', 'world:='+world_file],
            output='screen'
        ),

        # Lanzar robot_state_publisher con la descripción
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[robot_description]
        ),

        # Crear la entidad en Ignition Gazebo leyendo el robot del topic robot_description
        Node(
            package='ros_gz_sim',
            executable='create',
            output='screen',
            arguments=['-topic', 'robot_description', '-name', 'brazo', '-z', '0.1']
        )
    ])
