#!/usr/bin/env python

# Author: Hyeonjun Park, Ph.D. candidate
# Affiliation: Human-Robot Interaction LAB, Kyung Hee University, South Korea
# koreaphj91@gmail.com
# init: 9 Apr 2019
# revision: 17 Feb 2020


import sys
import rospy
import tf
import moveit_commander  # https://answers.ros.org/question/285216/importerror-no-module-named-moveit_commander/
import random
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped
from math import pi
from tf.transformations import quaternion_from_euler

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("move_group_python_interface_tutorial", anonymous=True)


# We get the joint values from the grougroup_name = "panda_arm"
group_name = "manipulator"
move_group = moveit_commander.MoveGroupCommander(group_name)
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -pi/2
joint_goal[1] = -pi/2
joint_goal[2] = 0
joint_goal[3] = -pi/2
joint_goal[4] = pi/2
joint_goal[5] = 0  # 1/6 of a turn

# The go command can be called with joint values, poses, or without any
# parameters if you have already set the pose or joint target for the group
move_group.go(joint_goal, wait=True)

# Calling ``stop()`` ensures that there is no residual movement
move_group.stop()

moveit_commander.roscpp_shutdown()