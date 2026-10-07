import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution


def generate_launch_description():
    # --------------------------------------------------------------------------
    # 1. Directories & Package Share Paths
    # --------------------------------------------------------------------------
    # NOTE: Replace 'my_robot_navigation' with your actual ROS 2 package name
    pkg_share = get_package_share_directory('robot_bringup')
    nav2_bringup_share = get_package_share_directory('nav2_bringup')

    # Default file paths inside your package
    default_map_path = PathJoinSubstitution([pkg_share, 'maps', 'my_map.yaml'])
    default_params_path = PathJoinSubstitution([pkg_share, 'config', 'nav2_params.yaml'])

    # --------------------------------------------------------------------------
    # 2. Launch Configurations
    # --------------------------------------------------------------------------
    map_yaml_file = LaunchConfiguration('map')
    params_file = LaunchConfiguration('params_file')
    use_sim_time = LaunchConfiguration('use_sim_time')
    autostart = LaunchConfiguration('autostart')

    # --------------------------------------------------------------------------
    # 3. Declare Launch Arguments
    # --------------------------------------------------------------------------
    declare_map_yaml_cmd = DeclareLaunchArgument(
        'map',
        default_value=default_map_path,
        description='Full path to map yaml file to load'
    )

    declare_params_file_cmd = DeclareLaunchArgument(
        'params_file',
        default_value=default_params_path,
        description='Full path to the ROS 2 Nav2 parameters YAML file'
    )

    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true'
    )

    declare_autostart_cmd = DeclareLaunchArgument(
        'autostart',
        default_value='true',
        description='Automatically startup the Nav2 lifecycle nodes'
    )

    # --------------------------------------------------------------------------
    # 4. Include Official Nav2 Bringup Launch
    # --------------------------------------------------------------------------
    nav2_bringup_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_share, 'launch', 'bringup_launch.py')
        ),
        launch_arguments={
            'map': map_yaml_file,
            'params_file': params_file,
            'use_sim_time': use_sim_time,
            'autostart': autostart,
            'use_docking': 'false',
        }.items()
    )

    # --------------------------------------------------------------------------
    # 5. Build Launch Description
    # --------------------------------------------------------------------------
    ld = LaunchDescription()

    # Add arguments
    ld.add_action(declare_map_yaml_cmd)
    ld.add_action(declare_params_file_cmd)
    ld.add_action(declare_use_sim_time_cmd)
    ld.add_action(declare_autostart_cmd)

    # Add node action
    ld.add_action(nav2_bringup_launch)

    return ld