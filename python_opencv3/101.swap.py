
import numpy as np
import cv2

#-- read pixels to ndarray
im1 = cv2.imread('../images/img001.png')
#im3 = np.empty_like(im1)



#-- pixel operation
# r = im1[:, :, 2]
# g = im1[:, :, 1]
# b = im1[:, :, 0]
# 
# im3[:, :, 2] = g
# im3[:, :, 1] = b
# im3[:, :, 0] = r

im3 = im1[:, :, (2,0,1)]


#-- save to png
cv2.imwrite('z101.png', im3)



