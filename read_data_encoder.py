#!/usr/bin/env python

import rospy #type: ignore
from std_msgs.msg import Int32  # Thay đổi kiểu dữ liệu nếu cần #type: ignore

def encoder_callback(data):
    rospy.loginfo("Received encoder data: %d", data.data)
    # Bạn có thể xử lý dữ liệu ở đây

def listener():
    rospy.init_node('encoder_listener', anonymous=True)
    rospy.Subscriber('/wheel/encoder', Int32, encoder_callback)

    # Chờ đợi và xử lý callback
    rospy.spin()

if __name__ == '__main__':
    listener()
