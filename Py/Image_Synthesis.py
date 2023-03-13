import numpy as np
import cv2

src1=cv2.imread("C:/Park/Src/dog.jpg")
src1=src1[500:725, 500:725] #이미지의 크기를 같게 해야함
src2=cv2.imread("C:/Park/Src/CarNum.jpg")
for i in range(11):
    alpha = i * 0.1
    beta = 1 - alpha
    dst = cv2.addWeighted(src1, alpha, src2, beta, 0)
    cv2.imshow("Image Synthesis", dst)
    cv2.waitKey(0)
cv2.destroyAllWindows()