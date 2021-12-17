"""Example to grasp an object at a specific pose"""
#!/usr/bin/env python

from niryo_one_python_api.niryo_one_api import *
import rospy
import math
rospy.init_node('niryo_one_run_python_api_code')


gripper_speed = 500

n = NiryoOne()

#n.calibrate_auto()

try:
    n.move_pose(0., 0.25, 0.40, 0., math.radians(90), math.radians(90)) #x,y,z , roll, pitch, yaw
    n.wait(0.2)
    n.open_gripper(TOOL_GRIPPER_1_ID, gripper_speed)
    n.open_gripper(TOOL_GRIPPER_1_ID, gripper_speed)

    n.move_pose(0., 0.25, 0.11, 0., math.radians(90), math.radians(90)) #move down

    n.close_gripper(TOOL_GRIPPER_1_ID, gripper_speed) #grasp
    n.close_gripper(TOOL_GRIPPER_1_ID, gripper_speed) #grasp
    #n.grab_with_tool(TOOL_GRIPPER_1_ID)

    n.move_pose(0., 0.25, 0.21, 0., math.radians(90), math.radians(90)) #move up

    joint_list = n.get_joints()
    joint_list[0] = 0 # rotate base joint, i.e., joint 1, to return to original position

    n.move_joints(joint_list)
    # n.shift_pose(AXIS_Z,0.14)
    #n.open_gripper(std_gripper, gripper_speed) # release object
    n.release_tool(TOOL_GRIPPER_1_ID)

    n.activate_learning_mode(True) # arm in rest position

except NiryoOneException as e:
    print "There was an issue"
    print e