
from PIL import Image
import numpy as np

#-- read pixels to ndarray
im0  = np.array(Image.open('../images/img001.png').convert('RGB'))
im3f = im0.astype(np.float64)


#-- pixel operation
width = im0.shape[1]

light = np.linspace(0, 255, width)

upr = 255
im3f[:,:,0] = np.minimum(im3f[:,:,0] + light, upr)
im3f[:,:,1] = np.minimum(im3f[:,:,1] + light, upr)
im3f[:,:,2] = np.minimum(im3f[:,:,2] + light, upr)


#-- save to png
Image.fromarray(np.uint8(im3f)).save('z110.png')


