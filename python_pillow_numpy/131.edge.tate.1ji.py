
from PIL import Image
import numpy as np

im1 = Image.open('../images/img002.png').convert('L')
width, height = im1.size
im1nd = np.array(im1)
im3 = Image.new('L', (width, height))

#-- filter coeff
d = 1
k = np.array([ 0,-1, 0,
               0, 1, 0,
               0, 0, 0 ])

#-- canvas loop
for y in range(d, height-d):
    for x in range(d, width-d):

        #-- get window
        w = im1nd[y-d:y+d+1, x-d:x+d+1].flatten()

        #-- filter
        s = int(w.dot(k)) + 128

        #-- put
        im3.putpixel((x, y), s)

im3.save('z131.png')


