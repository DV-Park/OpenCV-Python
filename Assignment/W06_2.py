import numpy as np, cv2

# 열림 연산은 배경의 잡영을 제거함과 동시에 팽창연산을 통하여 객체를 원래 크기로 돌려놓아 구분이 명확해졌습니다.
# 그에 비해 닫힘 연산은 위 번호판 이미지에선 객체의 내부를 채울 필요도 없었고, 배경의 잡영을 제거하는데에도 효과적이지 않았습니다.
# 닫힘 연산은 내부의 잡영이 많거나 객체의 형태와 크기는 보존하되, 작은 구멍들을 매울 수 있어 윤곽선을 부드럽게 만들 수 있습니다.

image = cv2.imread("../Src/CarNum.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

#마스크 선언 및 초기화

data=[0,1,0,1,1,1,0,1,0]
mask=np.array(data,np.uint8).reshape(3,3)
th_img=cv2.threshold(image,128,255,cv2.THRESH_BINARY)[1]

open_img=cv2.morphologyEx(th_img, cv2.MORPH_OPEN, mask)
close_img=cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask)
inner_img=cv2.morphologyEx(th_img, cv2.MORPH_TOPHAT, mask)
outer_img=cv2.morphologyEx(th_img, cv2.MORPH_BLACKHAT, mask)
gradient_img=cv2.morphologyEx(th_img, cv2.MORPH_GRADIENT, mask)

cv2.imshow("image",image)
cv2.imshow("binary image",th_img)
cv2.imshow("Open image",open_img)
cv2.imshow("Close image",close_img)
cv2.imshow("Tophat image",inner_img)
cv2.imshow("Blackhat image",outer_img)
cv2.imshow("Gradient image",gradient_img)
cv2.waitKey(0)
