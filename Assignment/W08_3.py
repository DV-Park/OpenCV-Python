import cv2
import numpy as np

img = cv2.imread("../Src/TestFlower.jpg")
rows,cols,ch=img.shape

pts1=np.float32([[100,50],[200,50],[100,100]])
pts2=np.float32([[100,150],[200,100],[100,200]])

cv2.circle(img,(100,50),5,(255,0,0),-1)
cv2.circle(img,(200,50),5,(0,255,0),-1)
cv2.circle(img,(100,100),5,(0,0,255),-1)

M=cv2.getAffineTransform(pts1,pts2)
dst=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("img",img)
cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()