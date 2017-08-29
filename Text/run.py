# create own image with drawing
import numpy as np
import cv2

# initialize image array
pic = np.zeros((500, 500, 3), dtype='uint8')  # uint8 means 0 - 255
color = (255, 255, 255)
font = cv2.FONT_HERSHEY_DUPLEX

cv2.putText(pic, 'A Text', (10, 250), font, 3, color, 5, cv2.LINE_8)

cv2.imshow('Text', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()