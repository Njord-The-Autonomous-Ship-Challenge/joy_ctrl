#!/usr/bin/env python2

import rospy

from ros_clients.msg import GeneralizedForce
from sensor_msgs.msg import Joy

def callback(msg):
    ctrl_pub = rospy.Publisher('force_control', GeneralizedForce, queue_size=1)

    force_output = GeneralizedForce(
        x = (msg.axes[2]-msg.axes[5])*50,
        y = -msg.axes[3]*100,
        z = 0,
        k = 0,
        m = 0,
        n = -msg.axes[0]*100
    )
    ctrl_pub.publish(force_output)

def listener():

    joy_subscriber = rospy.Subscriber("joy", Joy, callback, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('joy_controller', anonymous=True)
    listener()
