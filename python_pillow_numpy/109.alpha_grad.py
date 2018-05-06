
from PIL import Image
import numpy as np

#-- read pixels to ndarray
im0  = np.array(Image.open('../images/img001.png').convert('RGBA'))
im3f = im0.astype(np.float64)


#-- pixel operation
width = im0.shape[1]
alpha = np.linspace(0, 255, width)

im3f[:,:,3] = alpha



#-- save to png
Image.fromarray(np.uint8(im3f)).save('z109.png')


