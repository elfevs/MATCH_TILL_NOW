#!/urs/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

def pose_callback(pose_message):
    
    global x ,y, yaw
    x= pose_message.pose.pose.position.x
    y= pose_message.pose.pose.position.y
    
    yaw = pose_message.pose.pose.orientation.z
    
    
def circular_motion (velocity_publisher, angular_vel, linear_vel):
    velocity_msg = Twist()
    rate = rospy.Rate(10)
    
    angular_vel = 0.3
    R = 0.5 
    d = 0.5
    r1 = R - d/2
    r2 = R + d/2
    
    linear_vel = angular_vel/r1
    
    velocity_msg.linear.x = linear_vel
    velocity_msg.linear.y = 0
    velocity_msg.angular.z= angular_vel
    
    