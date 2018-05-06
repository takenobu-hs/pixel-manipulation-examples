
from PIL import Image
import numpy as np


#-- read and convert
im1 = Image.open('../images/img002.png').convert('L')
im1nd = np.array(im1)
width, height = im1.size

im3 = np.zeros_like(im1nd)


#-- filter coeff
d = 1
k = np.array([[ 0,-1, 0,],
              [ -1, 4,-1],
              [  0,-1, 0 ]])

#-- canvas loop
for y in range(d, height-d):
    for x in range(d, width-d):

        #-- get window
        w = im1nd[y-d:y+d+1, x-d:x+d+1]

        #-- filter
#       s = np.clip(w.dot(k) + 128, 0, 255)
        s = np.clip(np.einsum('ij,ij', w, k) + 128, 0, 255)

        #-- put
        im3[y, x] = s


#-- save to png
Image.fromarray(np.uint8(im3)).save('z134c.png')


