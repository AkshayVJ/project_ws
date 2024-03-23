#!/usr/bin/env python3
import math
import time
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist


class EFK_MODEL_SELECTOR():
    
    def __init__(self):
        self.linvel=0.0
        self.angvel=0.0
        self.yaw =0.0
        self.old_linvel=0.0
        self.old_angvel=0.0
        self.old_yaw=0.0
        self.straight_model= Odometry()
        self.curve_model= Odometry()
        self.output_model= Odometry()
        self.old_output_model= Odometry()
        self.init_node()
                

    def model_selector(self):
        
        dt_linvel=abs(self.linvel-self.old_linvel)
        dt_angvel=abs(self.angvel-self.old_angvel)

        if(self.linvel!=0 and self.angvel==0 and dt_linvel==0):
            self.output_model=self.straight_model
            print("Switched to Straigh Model")
        elif(self.angvel!= 0 and self.linvel==0 and dt_angvel==0):
            self.output_model=self.curve_model
            print("Switched to Curve Model")
        elif(self.linvel!=0 and self.angvel!=0 and self.linvel>=self.angvel):
            self.output_model=self.straight_model
            print("Switched to Straigh Model")    
        elif(self.angvel!= 0 and self.linvel!=0 and self.angvel>self.linvel):
            self.output_model=self.curve_model
            print("Switched to Curve Model") 
        else:
            self.output_model=self.old_output_model
            print("Default Model")   

        self.old_output_model=self.output_model
        self.old_linvel=self.linvel
        self.old_angvel=self.angvel


    def init_node(self):
        rospy.init_node("EKF_Model_Selector", anonymous=False)
        rospy.Subscriber("/cmd_vel", Twist, self.callback_cmd_vel)
        rospy.Subscriber("/odometry/filtered_global_straight", Odometry, self.callback_straight_model)
        rospy.Subscriber("/odometry/filtered_global_curve", Odometry, self.callback_curve_model)
        pub = rospy.Publisher("/odometry/filtered_global", Odometry, queue_size=10)
        self.old_output_model=self.straight_model
        rate=rospy.Rate(10) # 10hz
        
        while not rospy.is_shutdown():
            self.model_selector()
            pub.publish(self.output_model)
            rate.sleep()
        rospy.spin()         

    def callback_cmd_vel(self,data):
        self.linvel = abs(data.linear.x)
        self.angvel = abs(data.angular.z)
        
    def callback_straight_model(self,data):
        self.straight_model = data
         
    def callback_curve_model(self,data):
        self.curve_model = data 
            
if __name__ == '__main__':
    
    try:
        EFK_MODEL_SELECTOR()
    except rospy.ROSInterruptException:
        pass




