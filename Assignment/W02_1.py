import numpy as np
import cv2

image=cv2.imread("C:/Park/Src/dog.jpg")
if image is None: raise Exception("영상 파일 읽기 오류")

# cv2.imshow("original image",image)

height, width, channel = image.shape
dimensions = image.size

print("영상의 너비 =", height, ",높이 =",width)
print("영상의 채널 개수 =", channel)
print("영상의 화소 개수 =", dimensions)

cv2.waitKey(0)
cv2.destroyAllWindows()