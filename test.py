#%matplotlib inline
import cv2
import numpy as np

img=cv2.imread('./test.png', 0)

edges = cv2.Canny(img, 30, 70)    # canny边缘检测
cv2.imshow('canny', np.hstack((img, edges)))
cv2.waitKey(0)

