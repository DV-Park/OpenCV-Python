import numpy as np, cv2

# 열림연산을 통해 배경 잡영을 제거하고, 닫힘연산을 통해 내부의 잡영을 채워넣어 잡영을 제거하였습니다.

image = cv2.imread("../Src/noise_pepper.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

image2 = cv2.imread("../Src/noise_salt.jpg", cv2.IMREAD_GRAYSCALE)
if image2 is None: raise Exception("영상 파일 읽기 오류")

image3 = cv2.imread("../Src/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image3 is None: raise Exception("영상 파일 읽기 오류")

#마스크 선언 및 초기화

data=[0,1,0,1,1,1,0,1,0]
mask=np.array(data,np.uint8).reshape(3,3)
th_img=cv2.threshold(image,128,255,cv2.THRESH_BINARY)[1]

open_img=cv2.morphologyEx(th_img, cv2.MORPH_OPEN, mask)
result_img=cv2.morphologyEx(open_img, cv2.MORPH_CLOSE, mask)

th_img2=cv2.threshold(image2,128,255,cv2.THRESH_BINARY)[1]

open_img2=cv2.morphologyEx(th_img2, cv2.MORPH_OPEN, mask)
result_img2=cv2.morphologyEx(open_img2, cv2.MORPH_CLOSE, mask)

th_img3=cv2.threshold(image3,128,255,cv2.THRESH_BINARY)[1]

open_img3=cv2.morphologyEx(th_img3, cv2.MORPH_OPEN, mask)
result_img3=cv2.morphologyEx(open_img3, cv2.MORPH_CLOSE, mask)

cv2.imshow("image",image)
cv2.imshow("Result image",result_img)

cv2.imshow("image2",image2)
cv2.imshow("Result image2",result_img2)

cv2.imshow("image3",image3)
cv2.imshow("Result image3",result_img3)
cv2.waitKey(0)