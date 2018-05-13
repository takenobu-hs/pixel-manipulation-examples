
from PIL import Image
import numpy as np

#-- read pixels to ndarray
im1 = np.array( Image.open('../images/img001.png').convert('RGB') )
im3 = np.empty_like(im1)


#-- pixel operation
#gray = (im1[:, :, 0] + im1[:, :, 1] + im1[:, :, 2]) // 3
gray = im1[:, :, 0]//3 + im1[:, :, 1]//3 + im1[:, :, 2]//3

## im3[:, :, 0] = np.array(gray, dtype=np.uint8)
## im3[:, :, 1] = np.array(gray, dtype=np.uint8)
## im3[:, :, 2] = np.array(gray, dtype=np.uint8)

#gray = (im1[:, :, 0] + im1[:, :, 1] + im1[:, :, 2])
#gray = (im1[:, :, 0] + im1[:, :, 1] + im1[:, :, 2]) / 3

im3[:, :, 0] = gray
im3[:, :, 1] = gray
im3[:, :, 2] = gray


# im3[:, :, 0] = im3[:, :, 0] + im1[:, :, 2]
# im3[:, :, 0] = im3[:, :, 0] / 3
# im3[:, :, 1] = im3[:, :, 0]
# im3[:, :, 2] = im3[:, :, 0]



#-- save to png
Image.fromarray(im3).save('z102.png')
#imo = Image.fromarray(im3)
#imo.save('z101.png')


