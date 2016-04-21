import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__": 
    rospy.init_node('turtlebot_roomba')
    pub = rospy.Publisher('~cmd_vel', Twist, queue_size=5) 

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

            
            
            print 'i'
            # pick a random direction 
            #while not bumped into something 
            # move in that direction 
            # if bumped, break 
            

