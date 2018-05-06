
from PIL import Image
import numpy as np

#-- read pixels to ndarray
im0a  = np.array(Image.open('../images/img001.png').convert('RGB'))
im0b  = np.array(Image.open('../images/img002.png').convert('RGB'))
im3f = im0a.astype(np.float64)


#-- pixel operation
width = im0a.shape[1]
a = np.linspace(0, 1, width)

im3f[:,:,0] = (im0a[:,:,0] * a) + (im0b[:,:,0] * (1-a))
im3f[:,:,1] = (im0a[:,:,1] * a) + (im0b[:,:,1] * (1-a))
im3f[:,:,2] = (im0a[:,:,2] * a) + (im0b[:,:,2] * (1-a))





#-- save to png
Image.fromarray(np.uint8(im3f)).save('z112.png')


