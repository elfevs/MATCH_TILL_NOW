#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

x=0
y=0
yaw = 0
kL = 0.3

def go_goback_callback (msg):
    global x , y
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    orientation = msg.pose.pose.orientation
    orientation_list = [orientation.x, orientation.y, orientation.z, orientation.w]
    (roll, pitch,yaw) = euler_from_quaternion(orientation_list)

rospy.loginfo("agilex_go_straight")
sub = rospy.Subscriber("/mir1/mobile_base_controller/odom",Odometry,go_goback_callback)
pub = rospy.Publisher("/mir1/mobile_base_controller/cmd_vel", Twist, queue_size=10)

    
velocity_command = Twist()
rate = rospy.Rate(10)   
    
    
while not rospy.is_shutdown:
    
    x_goal = 1
    y_goal= 0        
    distance_x = (x_goal-x)
    distance_y = (y_goal-y)
    
    if distance_x > 0.1:
        velocity_command.linear.x = 0.3
        
    else:
        velocity_command.linear.x = 0.0
        if distance_y > 0.1:
            velocity_command.linear.y = 0.3
        else:
            velocity_command.linear.y = 0.0
            
    pub.publish(velocity_command)
    rate.sleep()
            
            
        
        