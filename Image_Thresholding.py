import numpy as np 
import cv2

img = cv2.imread('Logo.png', 0)

# define threshold value, if pixel value greater than this, then 1, otherwise 0
thresh = 200 # type 50 to see diffrence

(thresh_value, thresh_binary) = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

cv2.imshow('binary', thresh_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()