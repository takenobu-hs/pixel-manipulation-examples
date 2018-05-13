
from PIL import Image
import numpy as np


#-- read pixels to ndarray
im1 = np.array( Image.open('../images/img001.png').convert('RGB') )
im3 = np.empty_like(im1)


#-- pixel operation
r = im1[:, :, 0]
g = im1[:, :, 1]
b = im1[:, :, 2]

im3[:, :, 0] = g
im3[:, :, 1] = b
im3[:, :, 2] = r


#-- save to png
Image.fromarray(im3).save('z204.png')

