#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math
import time

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
        rospy.init_node('rotate_node', anonymous=True)
        rotate (10, 10 , True)
        time.sleep(1.0)
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")