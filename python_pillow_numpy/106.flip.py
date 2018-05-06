
from PIL import Image
import numpy as np

#-- read pixels to ndarray
im0  = np.array(Image.open('../images/img001.png').convert('RGB'))


#-- pixel operation
#im4 = im0[:,::-1,:]
im4 = im0[::-1,::-1,:]


#-- save to png
Image.fromarray(im4).save('z106.png')


