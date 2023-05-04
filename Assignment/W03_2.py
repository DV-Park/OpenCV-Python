import cv2
import matplotlib.pyplot as plt

def onChange(value):
    global image, title

    add_value=value-int(image[0][0])
    print("추가 화소값:", add_value)
    image=image+add_value
    th, dst = cv2.threshold(image, 130, 160, cv2.THRESH_BINARY)
    cv2.imshow(title, dst)

image=cv2.imread("../Src/dog.jpg", cv2.IMREAD_GRAYSCALE)
title="Thresh"
th, dst=cv2.threshold(image,130,160,cv2.THRESH_BINARY)
th, dst_O=cv2.threshold(image,-1,255,cv2.THRESH_OTSU)
th, dst_T=cv2.threshold(image,-1,255,cv2.THRESH_TRIANGLE)
print(th)

cv2.imshow(title, dst)
cv2.createTrackbar("Threshold",title,image[0][0],255,onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()