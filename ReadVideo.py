import numpy as np 
import cv2

capture = cv2.VideoCapture('SampleVideo.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
FPS = 60
frame_size = (720, 480)

out = cv2.VideoWriter('WrittenVideo', fourcc, FPS, frame_size)

while(capture.isOpened()):
  ret, frame = capture.read()
  cv2.imshow('Video', frame)
  if cv2.waitKey(0) & 0xFF == ord('q'):
    break
capture.release()
cv2.destroyAllWindows()