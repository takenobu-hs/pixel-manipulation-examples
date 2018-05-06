
from PIL import Image
import numpy as np

#-- read pixels to ndarray
im1f = np.array(Image.open('../images/img001.png').convert('RGB'), 'f')
im3f = np.empty_like(im1f)


#-- pixel operation
gray = im1f.mean(2)

im3f[:, :, :] = gray[:, :, np.newaxis]


#-- save to png
Image.fromarray(np.uint8(im3f)).save('z102h.png')

