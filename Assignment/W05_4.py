import cv2

image = cv2.imread("../Src/dog.jpg")
if image is None: raise Exception("영상 파일 읽기 오류")
cv2.imshow("srcImg",image)

ksize=(7,7)
dst1=cv2.boxFilter(image,-1,ksize)
cv2.imshow("boxFilter",dst1)

d=ksize[0]
sigmaColor=30.0     # 컬러 공간의 필터 표준 편차
sigmaSpace=30.0     # 좌표 공간의 필터 표준 편차
# d > 0 이면 sigmaSpace는 무시
# d < 0 이면 d=2x(3xsigmaSpace)+1

# dst2 는 d>0 이므로 edge 부분에선 적게, 이외의 부분에선 많이 블러링이 진행된다
# sigma 값을 올릴수록 편차의 허용범위가 커져 블러링이 더 많이 진행된다
dst2=cv2.bilateralFilter(image,d,sigmaColor,sigmaSpace)
cv2.imshow("Bilateral Filter",dst2)

# dst3 은 d<0 이므로 sigmaSpace에 의해 값이 결정된다
# 따라서 컬러 공간의 필터 값이 적용 되지 않아 강아지 이미지의 색이 블러링 되어 합쳐지는 것 처럼 보인다
dst3=cv2.bilateralFilter(image,-1,sigmaColor,sigmaSpace)
cv2.imshow("Bilateral Filter: sigmaSpace",dst3)
cv2.waitKey(0)
