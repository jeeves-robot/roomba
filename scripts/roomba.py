#!/usr/bin/env python

# Note: Need to source devel/setup.bash for this directory to get
# the package to be recognized

import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
from kobuki_msgs.msg import MotorPower
import random

topic = '/cmd_vel_mux/input/navi'

# This method is called when we hit something.
# Randomly choose a direction
def changeDirection(bump):
    print "Change direction!"

    if bump.state == BumperEvent.PRESSED:
        pub = rospy.Publisher(topic, Twist, queue_size=5)
        twist = Twist()
        angle = random.uniform(-1,1)
        twist.angular.x = angle 
        pub.publish(twist)
        twist.linear.x = 10
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
    
    motor = rospy.Publisher("/mobile_base/commands/motor_power", MotorPower, queue_size=1)
    power = MotorPower()
    power.state = 1
    motor.publish(power)
    # Subscribe to topic /mobile_base/events/bumper
    # to get notifications when we bump into things.
    sub = rospy.Subscriber('mobile_base/events/bumper', BumperEvent, changeDirection)
    print "Starting while loop"

    try: 
        while(1):	
            twist = Twist()
            twist.linear.x = 10 # this number is arbitrary 
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = 0
            pub.publish(twist)
    except:
        print "error!"
