
from PIL import Image
import numpy as np


#-- read and convert
im1 = Image.open('../images/img002.png').convert('RGB')
im1nd = np.array(im1)
width, height = im1.size

im3 = np.zeros_like(im1nd)


#-- filter coeff
d = 2
n = (d*2+1)*(d*2+1)

k = np.eye(5) / 5


#-- canvas loop
for y in range(d, height-d):
    for x in range(d, width-d):

        #-- get window
        w  = im1nd[y-d:y+d+1, x-d:x+d+1]

        #-- filter
        p = np.clip(np.einsum('yxc,yx->c', w, k), 0, 255)

        #-- put
        im3[y, x, :] = p


#-- save to png
Image.fromarray(np.uint8(im3)).save('z520b.png')

