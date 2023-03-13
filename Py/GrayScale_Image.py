import cv2
import numpy as np

# 명암도 영상 생성
img=np.zeros((50,512), np.uint8)
img2=np.zeros((50,512), np.uint8)
rows, cols=img.shape[:2]

for i in range(rows):
    for j in range(cols):
        img.itemset((i,j),j//2)
        img2.itemset((i,j),j//20*10)

cv2.imshow('Image', img)
cv2.imshow('Image2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()