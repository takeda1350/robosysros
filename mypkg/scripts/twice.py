#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import Int32

def cb(message):
	print(message.data * message.data)

if __name__ == '__main__':
	rospy.init_node('twice')
	sub = rospy.Subscriber('num', Int32, cb)
	rospy.spin()
