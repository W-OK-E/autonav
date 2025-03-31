# Build Workspace to see changes in Launch Files output
# chmod -R 755 /home/karthikeya/sim_ws/src/self_drive_course/models1
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable
def generate_launch_description():
    turtle_package = get_package_share_directory("turtlebot3_gazebo")
    gazebo_ros_package = get_package_share_directory('gazebo_ros')
    gazebo_launch_file = os.path.join(turtle_package, 'launch', 'turtlebot3_world.launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gazebo_launch_file),
        ),
    ])