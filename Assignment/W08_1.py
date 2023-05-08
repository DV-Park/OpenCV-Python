import cv2
import numpy as np
src=cv2.imread('../Src/TestFlower.jpg')
cv2.imshow("src",src)
h, w = src.shape[:2]

t_mat =np.array([[1,0,100],[0,1,-50]],dtype=np.float32)
dst=cv2.warpAffine(src,t_mat,dsize=(0,0))
cv2.imshow("Translation",dst)

s_mat=np.array([[2,0,0],[0,2,0]],dtype=np.float32)
dst=cv2.warpAffine(src,s_mat,dsize=(w*2,h))
cv2.imshow("Scaling",dst)

angle=30
cosa=np.cos(angle*np.pi/180.)
sina=np.sin(angle*np.pi/180.)
r_mat=np.array([[cosa,-sina,0],[sina,cosa,0]],dtype=np.float32)

print(r_mat)
dst=cv2.warpAffine(src,r_mat,dsize=(0,0))
cv2.imshow("Rotation (0,0)",dst)

cv2.waitKey()
cv2.destroyAllWindows()