
import numpy as np
import cv2

#-- read pixels to ndarray
im1 = cv2.imread('../images/img001.png')


#-- pixel operation
#    OpenCV: (B,G,R)
im1[:, :, (1,2)] = 0


#-- save to png
cv2.imwrite('z100b.png', im1)


