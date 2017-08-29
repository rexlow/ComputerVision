import numpy as np 
import cv2

img = cv2.imread('Logo.png') # 0

row = img.shape[0]
col = img.shape[1]

# shift 150 on x, 70 on y
Translation_Matrix = np.float32([[1, 0, 150], [0, 1, 70]])

shift = cv2.warpAffine(img, Translation_Matrix, (col, row))

cv2.imshow('shift', shift)
cv2.waitKey(0)
cv2.destroyAllWindows()