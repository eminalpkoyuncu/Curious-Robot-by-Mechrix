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
git hub. In the package, "ettir.py" consists of an UR3e application consisting of a collision check application with the physical workspace (consisting of a table, computer screen and gripper) whereas "li.py" consists of a face tracking application with image processing. "li.py" needs to be developed further and may not work as assumed. In order to use "li.py", an image data publisher Raspberry Pi is also needed and the details of the ROS application for this device is given in section 3.2. Note that the package "cv_basics" is included for the trial purposes and you can check your communication between the computer and Raspberry Pi using that package. 

HINT: Be careful while giving movement to the robot. Don't be afraid to smash the emergency button.

Useful link: https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/usage_example.md
  

**3.1) ROS1 Noetic simulation for UR3e**

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
rosrun hareket home.py
rosrun hareket ettir.py
```
Similar tutorail can be done with FRANKA EMIKA Panda robot.

Useful link: https://ros-planning.github.io/moveit_tutorials/

**3.2) ROS1 Noetic real-time control for UR3e**

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

e) To run the Moveit simulation (2nd Terminal)

```
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
roslaunch ur3e_moveit_config ur3e_moveit_planning_execution.launch 
```

f) To run the Rviz simulation (3rd Terminal)

```
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
roslaunch ur3e_moveit_config moveit_rviz.launch rvviz_config:=$(rospack find ur3e_moveit_config)/launch/moveit.rviz
```

g) To run a Python code to directly control the robot (4th Terminal)

```
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
rosrun hareket home.py
rosrun hareket ettir.py
```

h) Set up Raspberry Pi 

Assuming that the Raspberry Pi is booted for the first time and operating headless (without a monitor), the first step is to write the image of the operating system, which will run on the Raspberry Pi, to the SD card. Download "rpi-imager" software to your computer following the steps in this link: https://www.cyberithub.com/how-to-install-raspberry-pi-imager-on-ubuntu-20-04-lts/. After running "rpi-imager" select Ubuntu 20.04 Server as the operating system and write the image to the SD Card. You can refer to https://roboticsbackend.com/install-ubuntu-on-raspberry-pi-without-monitor/ for the headless setup of the Raspberry Pi. You should SSH into Raspberry Pi and install a desktop to the device after the setup is complete (xubuntu desktop is used during the project) for the image processing. After the desktop is installed, you should install xrdp for the remote desktop application (refer to https://tecadmin.net/how-to-install-xrdp-on-ubuntu-20-04/). After you install xrdp, you can access your Raspberry Pi desktop using a remote desktop provider such as "remmina" from your computer. When you reach your desktop environment, you should install ROS Noetic to your Raspberry Pi following the usual tutorial. For the application, OpenCV library should be installed to your Raspberry Pi (https://linuxize.com/post/how-to-install-opencv-on-ubuntu-20-04/). After the setup is complete, download "catkin_ws_rasp" folder to your Raspberry Pi device and copy the package to your workspace and build it. For the ROS communication between the Raspberry Pi and the ground station (main computer) follow the tutorial https://kashishdhal.me/ros-communication-between-different-computers/. Note that you can run the package "cv_basics" or "hareket li.py" on the main computer to subscribe to the Raspberry Pi. 


i) To run a Python code to face tracking (4th Terminal on the Computer)

```
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
rosrun hareket home.py
rosrun hareket li.py
```
**3.3) ROS2 Foxy demo simulation for UR3e**

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
**3.4) ROS2 Foxy real-time control for UR3e**

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
Useful source PDF: http://www.ritsumei.ac.jp/~kawamura/doc/ros2_ur.pdf

**4) Learning the basics of ROS**

In order to start moving your UR model freely with ROS you need to first familiarize yourself with the basics of ROS. Official tutorials for ROS
is a great place to start learning.

HINT: Before getting into creating your own ROS packages to control UR you should have at least followed the beginner level ROS tutorials until "Writing a simple
publisher and subscriber". 

Useful link: http://wiki.ros.org/ROS/Tutorials

**5) Learning the basics of Moveit**

Now that you have a basic understanding of how to use ROS you can should study the Moveit packages and try to understand how it works as most of your simple
kinematic solver functions are made via Moveit. Reading up until "Move Group Interface" section of the official moveit tutorials should be enough to have a basic 
understanding on the matter.

**6) Writing your own UR ROS control package**

Now you have almost all the tools you need to create and execute you own UR control packages. The section "Move Group Interface" has all the basic functions you might need. You can explore further how to effectively command this robot.

HINT: IF you are working with python as did we, move group python interface is a crucial source of information since after that section rest of the tutorials are written in C++. Absorb as much information as you can from these tutorials and other peoples examples such as the package that we have written for our project.

**Appendix**

Useful link for python interfacing:	

https://ros-planning.github.io/moveit_tutorials/doc/move_group_python_interface/move_group_python_interface_tutorial.html

Useful link for C++ interfacing: 

https://ros-planning.github.io/moveit_tutorials/doc/move_group_interface/move_group_interface_tutorial.html

Useful UR3e control with ROS1 Kinect youtube video: 

https://www.youtube.com/watch?v=b7rGA-Zsl3I 

Useful UR3e control with ROS1 Noetic repo: 

https://github.com/cambel/ur3/tree/noetic-devel

Useful UR3e control with ROS1 Noetic project and repo: 

https://sir.upc.edu/projects/rostutorials/final_work/

https://gitioc.upc.edu/rostutorials/ros2122-final-project

Useful ROS learning textbook "A Gentle Introduction to ROS": 

https://www.cse.sc.edu/~jokane/agitr/
