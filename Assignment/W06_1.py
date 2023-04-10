import numpy as np, cv2

# 팽창을 적용할시 선이 두꺼워지고 내부의 잡영이 없어졌고, 침식 적용시 선이 얇아졌습니다.
# 사용한 이미지의 경우 오히려 팽창을 통해서 잡영이 많이 사라진 모습을 볼 수 있습니다.

# 명도 영상에 적용 시 컬러값이 잡영으로 더 많이 나오게 되었습니다.

image = cv2.imread("../Src/CarNum.jpg")
if image is None: raise Exception("영상 파일 읽기 오류")

img = cv2.imread("../Src/CarNum.jpg", cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception("영상 파일 읽기 오류")

#마스크 선언 및 초기화

data=[0,1,0,1,1,1,0,1,0]
mask=np.array(data,np.uint8).reshape(3,3)
th_img=cv2.threshold(image,128,255,cv2.THRESH_BINARY)[1]

er_img=cv2.erode(th_img,mask)
di_img=cv2.dilate(th_img,mask)

th_img2=cv2.threshold(img,128,255,cv2.THRESH_BINARY)[1]

er_img2=cv2.erode(th_img2,mask)
di_img2=cv2.dilate(th_img2,mask)

cv2.imshow("image",image)
cv2.imshow("binary image",th_img)
cv2.imshow("OpenCV erode",er_img)
cv2.imshow("OpenCV dilate",di_img)

cv2.imshow("image2",img)
cv2.imshow("binary image2",th_img2)
cv2.imshow("OpenCV erode2",er_img2)
cv2.imshow("OpenCV dilate2",di_img2)
cv2.waitKey(0)