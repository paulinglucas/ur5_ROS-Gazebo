#!/usr/bin/env python



import rospy, sys, numpy as np
import geometry_msgs.msg
import moveit_msgs.msg
from ur5_notebook.msg import Tracker
from std_msgs.msg import Header
from std_msgs.msg import Bool
from std_srvs.srv import Empty

def gripper_status(msg):
    if msg.data:
        print('gripper status = {}'.format(msg.data))

def gripper_on():
    # Wait till the srv is available
    rospy.wait_for_service('/ur5/vacuum_gripper/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/ur5/vacuum_gripper/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper1_on():
    # Wait till the srv is available
    rospy.wait_for_service('/ur5/vacuum_gripper1/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/ur5/vacuum_gripper1/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper2_on():
    # Wait till the srv is available
    rospy.wait_for_service('/ur5/vacuum_gripper2/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/ur5/vacuum_gripper2/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper3_on():
    # Wait till the srv is available
    rospy.wait_for_service('/ur5/vacuum_gripper3/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/ur5/vacuum_gripper3/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper_off():
    rospy.wait_for_service('/ur5/vacuum_gripper/off')
    try:
        turn_off = rospy.ServiceProxy('/ur5/vacuum_gripper/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper1_off():
    rospy.wait_for_service('/ur5/vacuum_gripper1/off')
    try:
        turn_off = rospy.ServiceProxy('/ur5/vacuum_gripper1/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper2_off():
    rospy.wait_for_service('/ur5/vacuum_gripper2/off')
    try:
        turn_off = rospy.ServiceProxy('/ur5/vacuum_gripper2/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper3_off():
    rospy.wait_for_service('/ur5/vacuum_gripper3/off')
    try:
        turn_off = rospy.ServiceProxy('/ur5/vacuum_gripper3/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


def trigger(msg):
    gripper_trigger = msg.flag2
    if gripper_trigger:
        gripper_on()
        gripper1_on()
        gripper2_on()
        gripper3_on()
    else:
        gripper_off()
        gripper1_off()
        gripper2_off()
        gripper3_off()

rospy.init_node("ur5_gripper", anonymous=False)

gripper_status_sub = rospy.Subscriber('/ur5/vacuum_gripper/grasping', Bool, gripper_status, queue_size=1)

cxy_sub = rospy.Subscriber('cxy1', Tracker, trigger, queue_size=1)

rospy.spin()
