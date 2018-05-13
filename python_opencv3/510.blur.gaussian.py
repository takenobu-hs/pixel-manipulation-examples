
import numpy as np
import cv2


#-- read and convert
im1 = cv2.imread('../images/img002.png')
height = im1.shape[0]
width  = im1.shape[1]

im3 = np.zeros_like(im1)


#-- filter coeff
d = 2
n = (d*2+1)*(d*2+1)

kx = np.array([1, 4, 6, 4, 1])
ky = kx.reshape(5,1)
k = (kx * ky) / 256



#-- canvas loop
for y in range(d, height-d):

    if y % 10 == 0 : print(y)

    for x in range(d, width-d):

        #-- get window
        w  = im1[y-d:y+d+1, x-d:x+d+1]

        #-- filter
        p = np.clip(np.einsum('yxc,yx->c', w, k), 0, 255)

        #-- put
        im3[y, x, :] = p


#-- save to png
cv2.imwrite('z510.png', im3)

