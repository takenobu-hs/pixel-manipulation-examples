
import numpy as np
import cv2


#-- read pixels to ndarray
im0a = cv2.imread('../images/img001.png')
im0b = cv2.imread('../images/img002.png')
im3f = im0a.astype(np.float64)


#-- pixel operation
width = im0a.shape[1]
a = np.linspace(0, 1, width)

im3f[:,:,0] = (im0a[:,:,0] * a) + (im0b[:,:,0] * (1-a))
im3f[:,:,1] = (im0a[:,:,1] * a) + (im0b[:,:,1] * (1-a))
im3f[:,:,2] = (im0a[:,:,2] * a) + (im0b[:,:,2] * (1-a))


#-- save to png
cv2.imwrite('z232.png', im3f)

