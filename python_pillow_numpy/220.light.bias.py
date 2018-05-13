
from PIL import Image
import numpy as np

#-- read pixels to ndarray
im0  = np.array(Image.open('../images/img001.png').convert('RGB'), 'f')
im3f = np.empty_like(im0)


#-- pixel operation
s   = 70
upr = 255
im3f = np.minimum(im0 + s, upr)



#-- save to png
Image.fromarray(np.uint8(im3f)).save('z105.png')



