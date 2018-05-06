
from PIL import Image
import numpy as np

#-- read pixels to ndarray
im0  = np.array(Image.open('../images/img001.png').convert('RGB'))


#-- pixel operation
q = 64
im4 = (im0 // q) * q


#-- save to png
Image.fromarray(im4).save('z104.png')


