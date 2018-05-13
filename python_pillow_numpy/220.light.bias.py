
from PIL import Image
import numpy as np


#-- read pixels to ndarray
im0  = np.array(Image.open('../images/img001.png').convert('RGB'), 'f')
im3f = np.empty_like(im0)


#-- pixel operation
s   = 70
pmin = 0
pmax = 255

im3 = np.clip(im0 + s, pmin, pmax).astype(np.uint8)


#-- save to png
Image.fromarray(im3).save('z220.png')

