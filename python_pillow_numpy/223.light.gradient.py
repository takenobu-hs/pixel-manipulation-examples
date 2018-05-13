
from PIL import Image
import numpy as np

#-- read pixels to ndarray
im0  = np.array(Image.open('../images/img001.png').convert('RGB'))
im3f = im0.astype(np.float64)


#-- pixel operation
width  = im0.shape[1]
height = im0.shape[0]
light = np.tile( np.linspace(0, 255, width), (height,1) )

im3f = np.clip(im3f + light[:,:,np.newaxis], 0, 255)



#-- save to png
Image.fromarray(np.uint8(im3f)).save('z110b.png')


