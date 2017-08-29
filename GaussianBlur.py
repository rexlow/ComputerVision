import numpy as np 
import cv2

img = cv2.imread('Logo.png') # 0

matrix = (7, 7)
blur = cv2.GaussianBlur(img, matrix, 0)

cv2.imshow('blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()