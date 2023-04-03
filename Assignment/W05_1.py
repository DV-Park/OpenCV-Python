import cv2

# high 임계값을 먼저 조절 한 이후 low 임계값을 적절히 조절하면 에지 추적이 더 편리한 것 같습니다.

image = cv2.imread("../Src/CarNum.jpg")
if image is None: raise Exception("영상 파일 읽기 오류")

image2 = cv2.imread("../Src/AppleTree.jpg")
if image2 is None: raise Exception("영상 파일 읽기 오류")

image3 = cv2.imread("../Src/dog.jpg")
if image3 is None: raise Exception("영상 파일 읽기 오류")
canny=cv2.Canny(image,400,500)
canny2=cv2.Canny(image2,200,250)
canny3=cv2.Canny(image3,110,130)

cv2.imshow("image",image)
cv2.imshow("image2",image2)
cv2.imshow("image3",image3)
cv2.imshow("OpenCV_Canny",canny)
cv2.imshow("OpenCV_Canny2",canny2)
cv2.imshow("OpenCV_Canny3",canny3)
cv2.waitKey(0)
