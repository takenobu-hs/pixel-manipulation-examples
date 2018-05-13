
import numpy as np
import cv2


#-- read pixels to ndarray
im1 = cv2.imread('../images/img001.png')


#-- save to png
cv2.imwrite('z100.png', im1)

