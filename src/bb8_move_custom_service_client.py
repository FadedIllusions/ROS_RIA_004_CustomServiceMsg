#! /usr/bin/env python

# Import Needed Packages
import rospy
import rospkg
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest


# Init Node And Wait For Service
rospy.init_node('service_move_bb8_in_circle_custom_client')
rospy.wait_for_service('/move_bb8_in_circle_custom')

# Create Connection To Service
move_bb8_in_circle_service_client = rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage)

# Instantiate Request Object
move_bb8_in_circle_request_object = MyCustomServiceMessageRequest() 

# Set Duration
move_bb8_in_circle_request_object.duration = 5

rospy.loginfo("Performing Service Call...")

# Set And Print Result
result = move_bb8_in_circle_service_client(move_bb8_in_circle_request_object)
rospy.loginfo(str(result))

rospy.loginfo("-- END Of Service Call --")