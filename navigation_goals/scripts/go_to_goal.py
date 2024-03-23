#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math
import time

def go_to_goal(x_goal, y_goal):
    global x
    global y, z, yaw

    velocity_message = Twist()
    cmd_vel_topic='/cmd_vel'

    while (True):
        K_linear = 0.5 
        distance = abs(math.sqrt(((x_goal-x) ** 2) + ((y_goal-y) ** 2)))

        linear_speed = distance * K_linear

        K_angular = 4.0
        desired_angle_goal = math.atan2(y_goal-y, x_goal-x)
        angular_speed = (desired_angle_goal-yaw)*K_angular

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed

        velocity_publisher.publish(velocity_message)
        print( 'x=', x, 'y=',y)


        if (distance <0.01):
            break


if __name__ == '__main__':
    try:
        
        rospy.init_node('turtlesim_motion_pose', anonymous=True)
        go_to_goal(5,0)
        time.sleep(1.0)
        
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")