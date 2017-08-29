# median blur is used to remove noise from image
import numpy as np 
import cv2

img = cv2.imread('Logo.png') # 0

thresh_val1 = 50
thresh_val2 = 100

# all values below threshold value 1 are going to be 0, meaning black
# all values above threshold value 2 are going to be 1, meaning white
# this helps us to differentiate btw dark spot and white spot
canny = cv2.Canny(img, thresh_val1, thresh_val2)

cv2.imshow('CannyEdgeDetector', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()