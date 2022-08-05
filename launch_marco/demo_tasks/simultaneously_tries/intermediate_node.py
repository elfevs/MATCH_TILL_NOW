#!/usr/bin/env python


import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

vel_x= 0.0
vel_y = 0.0
yaw = 0.0



rospy.init_node("intermediate_node", anonymous=True)
pub = rospy.Publisher("/mir1/mobile_base_controller/cmd_vel", Twist, queue_size=10)
rate = rospy.Rate(10)

def intermediate_callback(msg):
    global vel_x, vel_y
    vel_msg = Twist()
    vel_x = vel_msg.linear.x
    vel_y = vel_msg.linear.y
    
    pub.publish(vel_msg)
    
    
def listener_and_pub():
    sub = rospy.Subscriber("mir1/mobile_base_controller/cmd_vel", Twist, intermediate_callback)
    rospy.spin()
    
if __name__=="__main__":
    try:
        listener_and_pub()
    except rospy.ROSInterruptException:
        pass
    
    
    
    
