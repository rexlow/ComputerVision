# create own image with drawing
import numpy as np
import cv2

# initialize image array
pic = np.zeros((500, 500, 3), dtype='uint8')  # uint8 means 0 - 255
color = (255, 255, 255)

# create a rectangle
# cv2.rectangle(
#   pic,             # image
#   (0, 0),          # point 1
#   (500, 150),      # point 2
#   (123, 200, 98),  # color
#   3,               # thickness
#   lineType=8,      # lineType
#   shift=0          # shift
# )

# draw a line
# cv2.line(pic, (200, 200), (500, 500), color)

# draw a circle
cv2.circle(pic, (250, 250), 100, color)

cv2.imshow('Image', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
