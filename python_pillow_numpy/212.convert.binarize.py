
from PIL import Image
import numpy as np


#-- read pixels to ndarray
im0  = np.array(Image.open('../images/img001.png').convert('L'))
im4 = np.empty_like(im0)


#-- pixel operation
hi = np.full_like(im0, 255)
lo = np.zeros_like(im0)

Th = 100
im4 = np.where(im0 > Th, hi, lo)


#-- save to png
Image.fromarray(im4).convert('RGB').save('z212.png')

