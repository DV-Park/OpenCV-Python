import numpy as np
import cv2

# src=cv2.imread("./Src/dog.jpg", cv2.IMREAD_GRAYSCALE)
# img1=cv2.multiply(src,2)
# img2=cv2.divide(src,2)
#
# dst=cv2.vconcat([src,img1,img2])
# cv2.imshow("Contrast Control", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

src1=cv2.imread("./Src/dog.jpg")
src2=cv2.imread("./Src/CarNum.jpg")
for i in range(11):
    alpha=i*0.1
    beta=1-alpha
    dst=cv2.addWeighted(src1,alpha,src2,beta,0)
    cv2.imshow("Image Synthesis", dst)
    cv2.waitKey(0)
cv2.destroyAllWindows()