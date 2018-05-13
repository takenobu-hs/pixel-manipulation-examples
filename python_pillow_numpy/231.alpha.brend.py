
from PIL import Image
import numpy as np

#-- read pixels to ndarray
im0a  = np.array(Image.open('../images/img001.png').convert('RGB'))
im0b  = np.array(Image.open('../images/img002.png').convert('RGB'))
im3f = im0a.astype(np.float64)


#-- pixel operation
a = 0.7

im3f = (im0a * a) + (im0b * (1-a))



#-- save to png
Image.fromarray(np.uint8(im3f)).save('z111.png')


