#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from tf import transformations



class Control():

    def __init__(self):

        self.sub_mir1_pos = rospy.Subscriber("/mir1/ground_truth", Odometry, self.callback_posion,"mir1")
        self.sub_mir2_pos = rospy.Subscriber("/mir2/ground_truth", Odometry, self.callback_posion,"mir2")
        self.sub_mir2_vel = rospy.Subscriber("/mir1/ground_truth", Odometry, self.velocity_callback)
        
        self.pub_mir2 = rospy.Publisher("/mir2/mobile_base_controller/cmd_vel", Twist, queue_size=10)
        
        self.odomdata = Odometry()
        self.command_velocity =Twist()


    def callback_posion(self, msg, robot_name):
        self.odomdata_x = msg.pose.pose.position.x
        self.odomdata_y = msg.pose.pose.position.y
        self.odomdata_z = msg.pose.pose.position.z



        self.odomdata_orientation = transformations.euler_from_quaternion([msg.pose.pose.orientation.x,msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w])
        self.odomdata_orientation_z= self.odomdata_orientation[2]
  

        if robot_name == "mir1":

            print ("x1:",self.odomdata_x, "[m]")
            print ("y1:",self.odomdata_y, "[m]")
            print ("orientation1:",math.degrees(self.odomdata_orientation_z), "°")

        elif robot_name == "mir2":

            print ("x2:",self.odomdata_x, "[m]")
            print ("y2:",self.odomdata_y, "[m]")
            print ("orientation2:",math.degrees(self.odomdata_orientation_z), "°")

        print ("-----------------------------------------------------------")
    

    def velocity_callback(self,msg):
        self.velocity_x = msg.twist.twist.linear.x
        self.velocity_y = msg.twist.twist.linear.y
        self.velocity_angular_z = msg.twist.twist.angular.z
        
        print("vel_x:",self.velocity_x,  "[m/s]")
        print("vel_y:",self.velocity_y, "[m/s]")
        print("vel_angular:",self.velocity_angular_z, "[rad/s]")

        print ("-----------------------------------------------------------")
        print ("-----------------------------------------------------------")
            
        if self.velocity_x != 0 and self.velocity_angular_z !=0:
            distance = 1
            self.command_velocity_x = self.velocity_x + self.velocity_angular_z * distance * (1 - 2* (math.cos(self.odomdata_orientation_z))**2 )
            self.command_velocity_y = 0        
            self.command_velocity_angular_z = self.velocity_angular_z
            
        self.pub_mir2.publish(self.command_velocity)

    
if __name__ == "__main__":
    rospy.init_node ("class_method") 
    control= Control()
    rospy.spin()












