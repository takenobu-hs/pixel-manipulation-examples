
from PIL import Image


#-- read pixels
im = Image.open('../images/img001.png').convert('RGB')


#-- save to png
im.save('z100.png')

