#! /usr/bin/env python

# Import Needed Packages
import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from geometry_msgs.msg import Twist


# Define Callback
def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle_custom Has Been Called")

    move_circle.linear.x = 0.2
    move_circle.angular.z = 0.2

    i=0
    while i <= request.duration:
        my_pub.publish(move_circle)
        rate.sleep()
        i+=1

    move_circle.linear.x = 0
    move_circle.angular.z = 0
    my_pub.publish(move_circle)
    rospy.loginfo("Finished Service move_bb8_in_circle_custom")

    response = MyCustomServiceMessageResponse()
    response.success = True

    return response

# Init Node
rospy.init_node("service_move_bb8_in_circle_custom_server")

# Instantiate Service And Publisher Objecgts
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage , my_callback)
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

# Instatiate Twist Object
move_circle = Twist()

# Define Rate
rate = rospy.Rate(1)

rospy.loginfo("Service /move_bb8_in_circle_custom Ready")
rospy.spin()