
import numpy as np
import cv2



#-- read and convert
im1 = cv2.imread('../images/img002.png', cv2.IMREAD_GRAYSCALE)


#-- filter coeff
d = 1
k = np.array([[ 0,-1, 0,],
              [ -1, 4,-1],
              [  0,-1, 0 ]])


#-- filter operation by cv3
im3 = np.clip(cv2.filter2D(im1, -1, k) + 128, 0, 255)


#-- save to png
cv2.imwrite('z410b.png', im3)

