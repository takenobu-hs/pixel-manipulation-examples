
import numpy as np
import cv2



#-- read and convert
im1 = cv2.imread('../images/img002.png', cv2.IMREAD_GRAYSCALE)
## height = im1.shape[0]
## width  = im1.shape[1]
## 
## im3 = np.zeros_like(im1)


#-- filter coeff
d = 1
k = np.array([[ 0,-1, 0,],
              [ -1, 4,-1],
              [  0,-1, 0 ]])


#-- filter operation by cv3

## NG! modulo?

#im3 = cv2.filter2D(im1, -1, k)
im3 = np.clip(cv2.filter2D(im1, -1, k) + 128, 0, 255)




## #-- canvas loop
## for y in range(d, height-d):
## 
##     if y % 10 == 0 : print(y)
## 
##     for x in range(d, width-d):
## 
##         #-- get window
##         w = im1[y-d:y+d+1, x-d:x+d+1]
## 
##         #-- filter
## #       s = np.clip(w.dot(k) + 128, 0, 255)
##         s = np.clip(np.einsum('ij,ij', w, k) + 128, 0, 255)
## 
##         #-- put
##         im3[y, x] = s


#-- save to png
cv2.imwrite('z234c.png', im3)


