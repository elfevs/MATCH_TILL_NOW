#!/usr/bin/env python


from click import command
import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion



x1 = x2 =0.0
y1 = y2 = 0.0
roll_1 = pitch_1 = yaw_1 = roll_2 = pitch_2 = yaw_2 = 0.0
kP = 1.0 
kL = 1.0



rospy.init_node("follow_mir_1")
pub_mir_2= rospy.Publisher("/mir2/mobile_base_controller/cmd_vel", Twist, queue_size=10)
sub_follow= rospy.Subscriber("/mir1/mobile_base_controller/cmd_vel", Twist, sub_follow)

speed = Twist()
rate = rospy.Rate(10)


while not rospy.is_shutdown():
    
    linear_distance = abs(x1-x2)
    angular_deviation = abs(yaw_1-yaw_2)
    Co= 0
    if linear_distance > 0.01:
        speed.linear.x = kL * linear_distance

    else:
        speed.linear.x = 0.0
    
    if angular_deviation > 0.1 :
        
        speed.angular.z = kP * angular_deviation

    else:
        
        speed.angular.z = 0.0

    print ("x1:", x1, "x2:", x2, "angular_deviation=", angular_deviation)


    pub_mir_2.publish(speed)
    rate.sleep()