from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'robot_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/config', ['config/gazebo_bridge.yaml', 'config/nav2_params.yaml']),
        ('share/' + package_name + '/launch', ['launch/sim_launch.xml' , 'launch/nav_launch.py']),
        ('share/' + package_name + '/worlds', ['worlds/home.sdf']),
        ('share/' + package_name + '/maps', ['maps/my_map.yaml', 'maps/my_map.pgm']),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='swayam',
    maintainer_email='swayam@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
