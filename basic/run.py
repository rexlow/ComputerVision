import numpy as np 
import cv2

img = cv2.imread('Logo.png', 0) # 0 returns gray
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()