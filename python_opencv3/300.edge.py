
import numpy as np
import cv2


#-- read and convert
im1 = cv2.imread('../images/img002.png')
im2 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)


#-- contours
ret, thresh = cv2.threshold(im2, 127, 255, 0)

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

im3 = cv2.drawContours(im2, contours, -1, (0,255,0), 3)

## 4th-1
## img = cv2.drawContours(img, contours, 3, (0,255,0), 3)
## 
## 4th-2
## cnt = contours[4]
## img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)



#-- save to png
cv2.imwrite('z300.png', im3)



