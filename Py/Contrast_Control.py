import numpy as np
import cv2

src=cv2.imread("C:/Park/Src/dog.jpg", cv2.IMREAD_GRAYSCALE)
img1=cv2.multiply(src,2)
img2=cv2.divide(src,2)

dst=cv2.vconcat([src,img1,img2])
cv2.imshow("Contrast Control", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()