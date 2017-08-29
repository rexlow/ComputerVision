import numpy as np 
import cv2

img = cv2.imread('noise.jpg') # 0

dim_pixel = 7
sigmaColor = 100 # consider more sigmaColor near the pixel
sigmaSpace = 100 # consider how far from the center pixel we are going to compute

filter = cv2.bilateralFilter(img, dim_pixel, sigmaColor, sigmaSpace)

cv2.imshow('BilateralFilter', filter)
cv2.waitKey(0)
cv2.destroyAllWindows()