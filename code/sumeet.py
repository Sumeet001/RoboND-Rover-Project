import cv2
import numpy as np
from matplotlib import pyplot as plt


example_grid = '../calibration_images/example_grid1.jpg'


img=cv2.imread(example_grid,0)

img1=cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

plt.imshow(img1)
plt.show()

ret1,thresh1 = cv2.threshold(img1,180,255,cv2.THRESH_TOZERO)


plt.imshow(thresh1*255)
plt.show()

