import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent

import random

# This method is called when we hit something.
# Randomly choose a direction
def changeDirection():
    pub = rospy.Publisher('~cmd_vel', Twist, queue_size=5)
    twist = Twist()
    twist.linear.x = 0.2
    twist.liear.y = 0
    twist.linear.z = 0
    twist.angular.x = random.uniform(-1, 1)
    twist.angular.y = 0
    twist.angular.z = 0
    pub.publish(twist)

if __name__ == "__main__": 
    rospy.init_node('turtlebot_roomba')
    pub = rospy.Publisher('~cmd_vel', Twist, queue_size=5) 

    # Subscribe to topic /mobile_base/events/bumper
    # to get notifications when we bump into things.
    sub = rospy.Subscriber('mobile_base/events/bumper', BumperEvent, changeDirection)

    try: 
        while(1):	
            twist = Twist()
            twist.linear.x = 0.2 # this number is arbitrary 
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = 0
            pub.publish(twist)
            # pick a random direction 
            #while not bumped into something 
            # move in that direction 
            # if bumped, break
