
import numpy as np
import cv2

im1 = cv2.imread('../images/img001.png')

im1 = 255 - im1

cv2.imwrite('z100.png', im1)


