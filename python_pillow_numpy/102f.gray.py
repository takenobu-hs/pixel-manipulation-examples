
from PIL import Image
import numpy as np

#-- read pixels to ndarray
im1f = np.array(Image.open('../images/img001.png').convert('RGB'), 'f')
im3f = np.empty_like(im1f)


#-- pixel operation
gray = im1f.sum(axis=2) / 3

im3f[:, :, 0] = gray
im3f[:, :, 1] = gray
im3f[:, :, 2] = gray


#-- save to png
Image.fromarray(np.uint8(im3f)).save('z102f.png')

