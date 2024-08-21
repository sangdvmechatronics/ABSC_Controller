#!/usr/bin/env python

import rospy #type: ignore
import rostopic #type: ignore

def callback(data):
    rospy.loginfo("Data type: %s", type(data))

if __name__ == '__main__':
    rospy.init_node('encoder_type_checker', anonymous=True)
    topic_type, _, _ = rostopic.get_topic_class('/wheel/encoder')
    rospy.Subscriber('/wheel/encoder', topic_type, callback)
    rospy.spin()
