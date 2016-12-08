import numpy as np
import cv2
import imutils
import math

cap = cv2.VideoCapture('rtmp://142.204.201.75:1935/javacam/mk01.stream')
# cap = cv2.VideoCapture('test.mp4')
# font = cv2.cvInitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font


def processFrame(frame):

	frame = imutils.resize(frame, width=min(600, frame.shape[1]))
	return frame


hog = cv2.CascadeClassifier('/usr/local/Cellar/opencv/2.4.12_2/share/OpenCV/haarcascades/haarcascade_fullbody.xml')



def findLast(rects):
	d1 = 0
	result = 0
	for (x,y,w,h) in rects:
		dist = distFromCenter(x, y)
		if dist > d1:
			d1 = dist
			result = (x,y,w,h)
	return result


def distFromCenter(x,y):
	return math.sqrt(x**2 + y**2)





while(1):
 	ret, frame = cap.read()
	frame = processFrame(frame)

	rects = hog.detectMultiScale(frame)
	filtered_rects = []
	for (x, y, w, h) in rects:
		print(x,y)
		if 150 < x < 450:
			filtered_rects.append((x,y,w,h))
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

	last = findLast(filtered_rects)

	if last:
		(x,y,w,h) = last
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)



	cv2.imshow('f',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break











cap.release()
cv2.destroyAllWindows()
