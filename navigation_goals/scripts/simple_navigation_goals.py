#!/usr/bin/env python3
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point


def move_to_goal(xgoal,ygoal,zgoal):
    
    ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    while(not ac.wait_for_server(rospy.Duration.from_sec(0.5))):
        rospy.loginfo("waiting for move base action server")

    goal = MoveBaseGoal()
    
    goal.target_pose.header.frame_id = "odom"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = xgoal
    goal.target_pose.pose.position.y = ygoal
    goal.target_pose.pose.position.z = 0
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = zgoal
    goal.target_pose.pose.orientation.w = 1.0
    print(goal)

    rospy.loginfo("Sending goal location ...")

    ac.send_goal(goal)
    ac.wait_for_result(rospy.Duration(200))

    if(ac.get_state()== GoalStatus.SUCCEEDED):
        rospy.loginfo("Goal Destination Reached!")
        return True
    else:
        rospy.loginfo("Robot Failed to Reach Destination!")
        return False

if __name__ == '__main__':
    rospy.init_node('Destination_Goal', anonymous=False)
    x_goal= 0
    y_goal= 0
    z_goal= -0.349
    print("Start go to goal")
    move_to_goal(x_goal,y_goal,z_goal)
    rospy.spin()
