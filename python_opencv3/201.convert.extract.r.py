
import numpy as np
import cv2

#-- read pixels to ndarray
im1 = cv2.imread('../images/img001.png')


#-- pixel operation
#    OpenCV: (B,G,R)
#    Pillow: (R,G,B)
im1[:, :, (0,1)] = 0
# im1[:, :, 2]


#-- save to png
cv2.imwrite('z100r.png', im1)


