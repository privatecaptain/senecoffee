
# import the necessary packages
import argparse
import datetime
import imutils
import time
import cv2


face_cascade = cv2.CascadeClassifier()
print face_cascade.load('/usr/local/Cellar/opencv/2.4.12_2/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')


def processFrame(frame):
	# frame = imutils.resize(frame,width=1280,height=720)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	return gray

# preview = cv2.namedWindow("javaCam Demo")

camera = cv2.VideoCapture('rtmp://142.204.201.75/its/javacam')
# camera = cv2.VideoCapture('')

# looping over the frames
while True:
	# grab the current frame and update the counter
	(success,frame) = camera.read()

	# Kill process, if no frames :(
	if not success:
		break

	# convert to grayScale and blur
	gray = processFrame(frame)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.imshow('test',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
