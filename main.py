import cv2
import numpy as np

img=cv2.imread('dog.jpg')
# img2=255-img
# img3=cv2.hconcat([img,img2])
img2=img+50
img3=cv2.add(img,50)
img=cv2.vconcat([img,img2,img3])
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
