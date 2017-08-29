import numpy as np 
import cv2

img = cv2.imread('Logo.png') # 0
# img = cv2.imwrite('SaveImage.png', img) # save image returns gray
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()