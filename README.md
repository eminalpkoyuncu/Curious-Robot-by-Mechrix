# Curious-Robot-by-Mechrix

This is a beginner's guide to Universal Robots ROS control guide. This should not be your only source while working on a UR model however, it can be used as a supplementary material that is created by our collective experience working on our project. All of the useful links and aliases that will be shared further in this document are the ones we used for our project which may differ from your preferences, but the steps remain more or less the same for different versions.

**1) Install and set up your ROS (For our case ROS Noetic is used)**

In theory you can use any distributions of the newer versions of ROS. Most of them are compatible with UR packages that is to be used however from our experience there was not enough study materials writing python codes with ROS2 so we chose to make our project using the newest version of ROS which was Noetic at the time.

HINT: Using binary builds (Debian packages for Ubuntu) is beneficial while using ROS, but don't forget to check whether your operating system is compatible with the ROS distribution you are trying to install. (For us it was Ubuntu 20.04 - ROS Noetic)

Useful link: http://wiki.ros.org/noetic/Installation/Ubuntu

**2) Create and set up your UR robot ROS workspace**

Creating the workspace and building it to operate your UR model can seem complicated at first but it is quite straightforward when
you are able to follow the instructions on the official ROS UR github page

HINT: Don't forget to change the branch name to your ROS distribution on the top left of the github page. (master usually means the latest distribution) 

HINT: fmauch is your friend

Useful link: https://github.com/UniversalRobots/Universal_Robots_ROS_Driver

**3) Usage and test drive of the UR**

Now that you successfully set up your UR ROS workspace you can run some test programs to move your robot following along the install page of the
git hub.

HINT: Be careful while giving movement to the robot. Don't be afraid to smash the emergency button.

Useful link: https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/usage_example.md
  

**3.1) ROS1 NOETIC SIMULATION for UR3e**

Previous link is summarized as

a) To source ROS1 Noetic (It is important to do it every time while working with ROS)

```
source /opt/ros/noetic/setup.bash
```

b) To run the  Universal Robot ROS packages for UR3e robot, changing the directory to that specific workspace and sourcing it should be done.

```
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
```

c) To run the Gazebo to simulate UR3e robot (1st Terminal)

```
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
roslaunch ur_gazebo ur3e_bringup.launch
```

d) To see the ROS nodes in schematic way with rqt graph (2nd Terminal)

```
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
rosrun rqt_joint_trajectory_controller rqt_joint_trajectory_controller
```

e) To run the Moveit simulation (3rd Terminal)

```
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
roslaunch ur3e_moveit_config ur3e_moveit_planning_execution.launch sim:=true
```

f) To run the Rviz simulation (4th Terminal)

```
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
roslaunch ur3e_moveit_config moveit_rviz.launch rvviz_config:=$(rospack find ur3e_moveit_config)/launch/moveit.rviz
```

g) To run a Python code to directly control the robot (5th Terminal)

```
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash

```
Similar tutorail can be done with FRANKA EMIKA Panda robot.

Useful link: https://ros-planning.github.io/moveit_tutorials/

**3.2) ROS1 NOETIC REAL-TIME CONTROL for UR3e**

a) To source ROS1 Noetic (It is important to do it every time while working with ROS)

```
source /opt/ros/noetic/setup.bash
```

b) To run the  Universal Robot ROS packages for UR3e robot, changing the directory to that specific workspace and sourcing it should be done.

```
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
```

c) To rlaunch up to UR3e robot (1st Terminal)

```
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=yyy.yyy.yyy.yyy
```

d) To see the ROS nodes in schematic way with rqt graph (2nd Terminal)

```
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
rosrun rqt_joint_trajectory_controller rqt_joint_trajectory_controller
```

e) To run the Moveit simulation (3rd Terminal)

```
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
roslaunch ur3e_moveit_config ur3e_moveit_planning_execution.launch 
```

f) To run the Rviz simulation (4th Terminal)

```
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
roslaunch ur3e_moveit_config moveit_rviz.launch rvviz_config:=$(rospack find ur3e_moveit_config)/launch/moveit.rviz
```

g) To run a Python code to directly control the robot (5th Terminal)

```
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
```
**3.3) ROS2 FOXY DEMO SIMULATION for UR3e**

As similar to ROS1 Noetic, ROS2 can be used to execute these practices. However, due to lack of sources, Python availability (it is only supporting C++ for controlling for now) and rapidly updating ROS2 versions it is not likely to have a stable working with ROS2 nowadays. Altough we started our studies with ROS2 Foxy which had LTS, ROS2 Humble becomes the new LTS version and availabilty of drivers have changed. The progress we made up to this point is provided as similar to previous tutorials.

a) To connect the UR3e robot with Rviz via computer in a simulated environment  (1st Terminal)

```
export COLCON_WS=~/workspace/ros_ur_driver
cd ~/workspace/ros_ur_driver
source install/setup.bash
ros2 launch ur_bringup ur_control.launch.py ur_type:=ur3e robot_ip:=yyy.yyy.yyy.yyy use_fake_hardware:=true launch_rviz:=true
```

b) To run the provided demo (2nd Terminal)

```
export COLCON_WS=~/workspace/ros_ur_driver
cd ~/workspace/ros_ur_driver
source install/setup.bash
ros2 launch ur_bringup test_joint_trajectory_controller.launch.py
```
**3.4) ROS2 FOXY REAL-TIME CONTROL for UR3e**

a) To source ROS2 Foxy (It is important to do it every time while working with ROS)

```
source /opt/ros/foxy/setup.bash
```

b) To run the  Universal Robot ROS packages for UR3e robot, changing the directory to that specific workspace, exporting and sourcing it should be done.

```
export COLCON_WS=~/workspace/ros_ur_driver
cd ~/workspace/ros_ur_driver
source install/setup.bash
```

c) To connect the UR3e robot with Rviz via computer to controlling the real robot (1st Terminal) 

```
export COLCON_WS=~/workspace/ros_ur_driver
cd ~/workspace/ros_ur_driver
source install/setup.bash
ros2 launch ur_bringup ur_control.launch.py ur_type:=ur3e robot_ip:=yyy.yyy.yyy.yyy use_fake_hardware:=true launch_rviz:=false
```

d) To start Moveit (2nd Terminal)

```
export COLCON_WS=~/workspace/ros_ur_driver
cd ~/workspace/ros_ur_driver
source install/setup.bash
ros2 launch ur_bringup ur_moveit.launch.py ur_type:=ur3e robot_ip:= yyy.yyy.yyy.yyy use_fake_hardware:=true launch_rviz:=true
```
