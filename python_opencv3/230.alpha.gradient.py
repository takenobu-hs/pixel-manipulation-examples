
import numpy as np
import cv2


#-- read pixels to ndarray
im0 = cv2.imread('../images/img001.png')


#-- pixel operation
width  = im0.shape[1]
height = im0.shape[0]
alpha = np.tile( np.linspace(0, 255, width), (height,1) )

im3f = np.dstack((im0, alpha))



#-- save to png
cv2.imwrite('z109.png', im3f)




