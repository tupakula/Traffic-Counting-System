import cv2

cap = cv2.VideoCapture("rtsp://192.168.1.52:8080/videoMain")
#cap = cv2.VideoCapture("flow.mp4")
while(1):
	ret, frame = cap.read()
	if ret == True:
		cv2.imshow("test", frame)
	key = cv2.waitKey(10)
