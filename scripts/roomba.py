#!/usr/bin/env python

# Note: Need to source devel/setup.bash for this directory to get
# the package to be recognized

import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
from kobuki_msgs.msg import MotorPower
import random
import time 

topic = '/cmd_vel_mux/input/navi'

# This method is called when we hit something.
# Randomly choose a direction
def changeDirection(bump):
    print "Change direction!"

    pub = rospy.Publisher(topic, Twist, queue_size=5)
    twist = Twist()

    # The TA told me to do something like this, but it's not quite working.
    # She basically said to keep calling rotate 10 times for a second or two. 
    # 
    if bump.state == BumperEvent.PRESSED:
        for i in range(50):
            twist.linear.x = -0.05
            twist.angular.x = 1
            pub.publish(twist)
            time.sleep(0.2)
        twist.linear.x = 0.05
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0#angle * -1
        twist.angular.y = 0
        twist.angular.z = 0
        pub.publish(twist)

if __name__ == "__main__": 
    print "Starting main"
    rospy.init_node('turtlebot_roomba')
    pub = rospy.Publisher(topic, Twist, queue_size=5)
 
    # Subscribe to topic /mobile_base/events/bumper
    # to get notifications when we bump into things.
    sub = rospy.Subscriber('mobile_base/events/bumper', BumperEvent, changeDirection)
    print "Starting while loop"

    try: 
        while(1):
            twist = Twist()
            twist.linear.x = 0.05
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = 0
            pub.publish(twist)
            time.sleep(0.2)
    except:
        print "error!"
