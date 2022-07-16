#!/usr/bin/env python3

# Import the necessary libraries
import rospy # Python library for ROS
from std_msgs.msg import Int16MultiArray # Image is the message type

import cv2
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images




def publish_message():

	face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


	# Node is publishing to the video_frames topic using 
	# the message type Image	s
	pub = rospy.Publisher('topic', Int16MultiArray, queue_size=10)

	# Tells rospy the name of the node.
	# Anonymous = True makes sure the node has a unique name. Random
	# numbers are added to the end of the name.
	rospy.init_node('video_pub_py', anonymous=True)

	# Go through the loop 10 times per second
	rate = rospy.Rate(10) # 10hz

	# Create a VideoCapture object
	# The argument '0' gets the default webcam.
	cap = cv2.VideoCapture(0)

	# Used to convert between ROS and OpenCV images
	br = CvBridge()

	# While ROS is still running.
	while not rospy.is_shutdown():

		# Capture frame-by-frame
		# This method returns True/False as well
		# as the video frame.
		ret, frame = cap.read()

		if ret == True:
			# Print debugging information to the terminal
			rospy.loginfo('publishing video frame')

			grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(grey,1.3,5)
			arg = Int16MultiArray()
			for(x,y,w,h) in faces:
				cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
				arg.data.append(int(x))
				arg.data.append(int(y))
				arg.data.append(int(w))
				arg.data.append(int(h))


			if cv2.waitKey(1) & 0xFF==ord("q"):
				break

			# Publish the data.
			pub.publish(arg)

		# Sleep just enough to maintain the desired rate
		rate.sleep()

if __name__ == '__main__':
	try:
		publish_message()
	except rospy.ROSInterruptException:
		pass
