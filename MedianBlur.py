# median blur is used to remove noise from image
import numpy as np 
import cv2

img = cv2.imread('noise.jpg') # 0

kernal = 3
median = cv2.medianBlur(img, kernal)

cv2.imshow('MedianBlur', median)
cv2.waitKey(0)
cv2.destroyAllWindows()