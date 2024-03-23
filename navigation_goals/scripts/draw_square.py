#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math
import time

def move_straight(speed, distance, is_forward):  

        distance_moved = 0.0
        t_old=0.0
        t_curr=0.0  
        
        velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        velocity_message = Twist()
        loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)  
        
        
        if (speed > 0.4):
            print('speed must be lower than 0.4')
            return

        if (is_forward):
            velocity_message.linear.x =abs(speed)
        else:
        	velocity_message.linear.x =-abs(speed)

        t_old = rospy.Time.now().to_sec()
        while True :

                rospy.loginfo("Robot is moving ")
                velocity_publisher.publish(velocity_message)
                loop_rate.sleep()
                t_curr =  rospy.Time.now().to_sec()
                #rospy.Duration(1.0)
                
                distance_moved = (t_curr-t_old) * speed
                print("Distance covered in meters :",distance_moved)              
                if  not (distance_moved<distance):
                    rospy.loginfo("Reached Destination")
                    break
        
        #finally, stop the robot when the distance is moved
        velocity_message.linear.x =0
        velocity_publisher.publish(velocity_message)
    

def rotate (angular_speed_degree, relative_angle_degree, clockwise):

    velocity_message = Twist()
    velocity_message.linear.x=0
    velocity_message.linear.y=0
    velocity_message.linear.z=0
    velocity_message.angular.x=0
    velocity_message.angular.y=0
    velocity_message.angular.z=0

    angular_speed=math.radians(abs(angular_speed_degree))

    if (clockwise):
        velocity_message.angular.z =-abs(angular_speed)
    else:
        velocity_message.angular.z =abs(angular_speed)

    angle_moved = 0.0
    t_old=0.0
    t_curr=0.0
    loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
    cmd_vel_topic='/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    t_old = rospy.Time.now().to_sec()

    while True :
        rospy.loginfo("Tortoisebot is rotating")
        velocity_publisher.publish(velocity_message)

        t_curr = rospy.Time.now().to_sec()
        current_angle_degree = (t_curr-t_old)*angular_speed_degree
        loop_rate.sleep()

        print('current_angle_degree: ',current_angle_degree)
                       
        if  (current_angle_degree>relative_angle_degree):
            rospy.loginfo("reached")
            break

    #finally, stop the robot when the distance is moved
    velocity_message.angular.z =0
    velocity_publisher.publish(velocity_message)

    
if __name__ == '__main__':
    try:
        rospy.init_node('move_straight_node', anonymous=True)
        move_straight(0.3, 5.0, True)
        time.sleep(1.0)
        rotate(30, 90, True)
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")