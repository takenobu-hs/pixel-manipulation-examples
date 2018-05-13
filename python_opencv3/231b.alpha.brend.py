
import numpy as np
import cv2


#-- read pixels to ndarray
im0a = cv2.imread('../images/img001.png')
im0b = cv2.imread('../images/img002.png')
im3f = im0a.astype(np.float64)


#-- pixel operation
a = 0.7

#im3f = (im0a * a) + (im0b * (1-a))
im3f = cv2.addWeighted(im0a, a, im0b, (1-a), 0)


#-- save to png
cv2.imwrite('z231b.png', im3f)

