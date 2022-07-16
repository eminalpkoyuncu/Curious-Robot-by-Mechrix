import rospy
import moveit_commander
import numpy as np
from geometry_msgs.msg import Pose
from actionlib import SimpleActionClient
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from lib import visual_servo_lib as vslib

class ur_control:
    def _init_(self, node_name, group_name,r_wp,beta_1,beta_2,beta_3,d_insp,a_insp,alpha):

        rospy.init_node(node_name, anonymous=False)
        self.group_name = group_name
        self.group = moveit_commander.MoveGroupCommander(group_name)
        self.active_joint_names = self.group.get_active_joints()
        self.end_effector = self.group.get_end_effector_link()
        print("End Effector Name: ", self.end_effector)
        r_bc_b, rho_bc, r_wb, rho_wb = vslib.move_robots(r_wp,beta_1,beta_2,beta_3,d_insp,a_insp,alpha)

        print("r_bc_b = ", r_bc_b.flatten())
        print("rho_bc = ", rho_bc.flatten())

        ur_pose_tar = r_bc_b.flatten().tolist()+rho_bc.flatten().tolist()
        # ur_pose_tar = [0.3,0,1.2,0,0,0,1]
        self.group.set_pose_target(ur_pose_tar)
        self.group.go()

node_name = "ur__base_node"
group_name = "manipulator"

arm_control = ur_control(node_name, group_name, r_wp,beta_1,beta_2,beta_3,d_insp,a_insp,alpha)
rospy.signal_shutdown("Shutdown")