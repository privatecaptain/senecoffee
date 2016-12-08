import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture('rtmp://142.204.201.75:1935/javacam/mk01.stream')
# cap = cv2.VideoCapture('test.mp4')
# font = cv2.cvInitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font


def processFrame(frame):

	frame = imutils.resize(frame, width=min(400, frame.shape[1]))
	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	gray = clahe.apply(gray)
	# th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

	return gray


fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
# _,bg = cap.read()

bg =cv2.imread('bg.png',1)
bg = processFrame(bg)

def filter():
	for i in range(100):
		frame,r = cap.read()

def reset():
	_,bg = cap.read()
	bg = processFrame(bg)

count = 0
filter()


while(1):
 	ret, frame = cap.read()
	frame = processFrame(frame)
 # 	subframe = cv2.subtract(frame, bg)
	fgmask = fgbg.apply(frame)

	# ret, thresh = cv2.threshold(subframe,127,255,cv2.THRESH_BINARY)
	th3 = cv2.adaptiveThreshold(fgmask,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
	# cv2.putText(frame, '4',(100,100),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,0))

	cv2.imshow('frame',frame)
	cv2.imshow('fgmask', fgmask)
	# cv2.imshow('thresh', thresh)
	cv2.imshow('adaptiveThreshold', th3)
	count += 1

	if count > 30:
		# reset()
		count = 0

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break



def cMog(frames):

	for frame in frames:
		pass









cap.release()
cv2.destroyAllWindows()
