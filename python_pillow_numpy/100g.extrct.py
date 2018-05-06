
from PIL import Image
import numpy as np

#-- read pixels to ndarray
im1 = np.array( Image.open('../images/img001.png').convert('RGB') )


#-- pixel operation
im1[:, :, 0] = 0
#im1[:, :, 1] = 0
im1[:, :, 2] = 0


#-- save to png
im3 = Image.fromarray(im1)
im3.save('z100g.png')


