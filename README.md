# Curious-Robot-by-Mechrix

ROS1 NOETIC SIMULATION for UR3e

1) To source ROS1 Noetic (It is important to do it every time while working with ROS)

'''

source /opt/ros/noetic/setup.bash

'''

2) To run the  Universal Robot ROS packages for UR3e robot, changing the directory to that specific workspace and sourcing it should be done.

cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash

3) To run the Gazebo to simulate UR3e robot (1st Terminal)

cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
roslaunch ur_gazebo ur3e_bringup.launch

4) To see the ROS nodes in schematic way with rqt graph (2nd Terminal)

cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
rosrun rqt_joint_trajectory_controller rqt_joint_trajectory_controller

5) To run the Moveit simulation (3rd Terminal)

cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
roslaunch ur3e_moveit_config ur3e_moveit_planning_execution.launch sim:=true


6) To run the Rviz simulation (4th Terminal)

cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
roslaunch ur3e_moveit_config moveit_rviz.launch rvviz_config:=$(rospack find ur3e_moveit_config)/launch/moveit.rviz

7) To run a Python code to directly control the robot (5th Terminal)

cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash

ROS1 NOETIC SIMULATION for Panda

1) To run the FRANKA EMIKA packages Panda Robot, changing the directory to that specific workspace and sourcing it should be done.

cd ~/ws_moveit
source ~/ws_moveit/devel/setup.bash

ROS2 FOXY REAL-TIME CONTROL for UR3e

1) To source ROS2 Foxy (It is important to do it every time while working with ROS)

source /opt/ros/foxy/setup.bash

2) To run the  Universal Robot ROS packages for UR3e robot, changing the directory to that specific workspace, exporting and sourcing it should be done.

export COLCON_WS=~/workspace/ros_ur_driver
cd ~/workspace/ros_ur_driver
source install/setup.bash

3) To connect the UR3e robot with Rviz via computer to controlling the real robot (1st Terminal) 

export COLCON_WS=~/workspace/ros_ur_driver
cd ~/workspace/ros_ur_driver
source install/setup.bash
ros2 launch ur_bringup ur_control.launch.py ur_type:=ur3e robot_ip:=yyy.yyy.yyy.yyy use_fake_hardware:=true launch_rviz:=false

4) To start Moveit (2nd Terminal)

export COLCON_WS=~/workspace/ros_ur_driver
cd ~/workspace/ros_ur_driver
source install/setup.bash
ros2 launch ur_bringup ur_moveit.launch.py ur_type:=ur3e robot_ip:= yyy.yyy.yyy.yyy use_fake_hardware:=true launch_rviz:=true

ROS2 FOXY DEMO SIMULATION for UR3e

1) To connect the UR3e robot with Rviz via computer in a simulated environment  (1st Terminal)

export COLCON_WS=~/workspace/ros_ur_driver
cd ~/workspace/ros_ur_driver
source install/setup.bash
ros2 launch ur_bringup ur_control.launch.py ur_type:=ur3e robot_ip:=yyy.yyy.yyy.yyy use_fake_hardware:=true launch_rviz:=true


2) To run the provided demo (2nd Terminal)

export COLCON_WS=~/workspace/ros_ur_driver
cd ~/workspace/ros_ur_driver
source install/setup.bash
ros2 launch ur_bringup test_joint_trajectory_controller.launch.py
