import numpy as np, cv2

image = cv2.imread("../Src/CarNum.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

img = cv2.imread("../Src/CarNum.jpg", cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception("영상 파일 읽기 오류")

#마스크 선언 및 초기화

data=[0,1,0,1,1,1,0,1,0]
mask=np.array(data,np.uint8).reshape(3,3)

er_img=cv2.erode(image,mask)
di_img=cv2.dilate(image,mask)

th_img2=cv2.threshold(img,128,255,cv2.THRESH_BINARY)[1]

er_img2=cv2.erode(th_img2,mask)
di_img2=cv2.dilate(th_img2,mask)

cv2.imshow("image",image)
cv2.imshow("OpenCV erode",er_img)
cv2.imshow("OpenCV dilate",di_img)

cv2.imshow("image2",img)
cv2.imshow("binary image2",th_img2)
cv2.imshow("OpenCV erode2",er_img2)
cv2.imshow("OpenCV dilate2",di_img2)
cv2.waitKey(0)