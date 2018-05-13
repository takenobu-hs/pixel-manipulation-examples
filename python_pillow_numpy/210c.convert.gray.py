
from PIL import Image
import numpy as np

#-- read pixels to ndarray
im0  = np.array(Image.open('../images/img001.png').convert('RGB'))
im1f = im0.astype(np.float64)
im3f = np.empty_like(im1f)


#-- pixel operation
gray = (im1f[:, :, 0] + im1f[:, :, 1] + im1f[:, :, 2]) / 3

im3f[:, :, 0] = gray
im3f[:, :, 1] = gray
im3f[:, :, 2] = gray


#-- save to png
im4 = im3f.astype(np.uint8)
Image.fromarray(im4).save('z102.png')


