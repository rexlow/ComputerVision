import numpy as np 
import cv2

img = cv2.imread('Logo.png') # 0

row = img.shape[0]
col = img.shape[1]

center = (col/2, row/2)
angle = 90

RotateMatrix = cv2.getRotationMatrix2D(center, angle, 1) # 1 is scale
rotate = cv2.warpAffine(img, RotateMatrix, (col, row))

cv2.imshow('rotate', rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()