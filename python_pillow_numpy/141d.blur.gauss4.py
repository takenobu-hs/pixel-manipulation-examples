
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

kx = np.array([1, 4, 6, 4, 1])
ky = kx.reshape(5,1)
k = (kx * ky) / 256



#-- canvas loop
for y in range(d, height-d):
    for x in range(d, width-d):

        #-- get window
        w  = im1nd[y-d:y+d+1, x-d:x+d+1]

        #-- filter
#       wr = np.clip((w[:,:, 0] * k).sum(), 0, 255)
#       wg = np.clip((w[:,:, 1] * k).sum(), 0, 255)
#       wb = np.clip((w[:,:, 2] * k).sum(), 0, 255)
#       wr = np.clip(np.einsum('ij,ij', w[:,:, 0], k), 0, 255)
#       wg = np.clip(np.einsum('ij,ij', w[:,:, 1], k), 0, 255)
#       wb = np.clip(np.einsum('ij,ij', w[:,:, 2], k), 0, 255)
        p = np.clip(np.einsum('yxc,yx->c', w, k), 0, 255)

        #-- put
#       im3[y, x, 0] = wr
#       im3[y, x, 1] = wg
#       im3[y, x, 2] = wb
        im3[y, x, :] = p


#-- save to png
Image.fromarray(np.uint8(im3)).save('z141d.png')


