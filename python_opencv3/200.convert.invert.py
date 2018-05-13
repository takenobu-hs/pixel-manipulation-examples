
import numpy as np
import cv2


#-- read pixels to ndarray
im1 = cv2.imread('../images/img001.png')


#-- pixel operation
im1 = 255 - im1


#-- save to png
cv2.imwrite('z200.png', im1)

