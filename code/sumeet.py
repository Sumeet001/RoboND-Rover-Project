import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as im

example_grid = '../calibration_images/example_grid1.jpg'


img=im.imread(example_grid)

img=img[:,:,::-1]
b,g,r=cv2.split(img)#, cv2.RBG2HSV)

plt.imshow(g)
plt.show()

plt.imshow(r)
plt.show()

plt.imshow(b)
plt.show()

ret1,thresh1 = cv2.threshold(img1,180,255,cv2.THRESH_TOZERO)


plt.imshow(thresh1*255)
plt.show()

