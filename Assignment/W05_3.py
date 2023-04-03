import numpy as np,cv2

image = cv2.imread("../Src/CarNum.jpg")
if image is None: raise Exception("영상 파일 읽기 오류")

# 1. 가우시만 마스크를 생성 kernel을 통하여 img를 필터링한다.
# 2. OpenCV에서 제공하는 가우시안 필터를 통하여 가우시안 블러링 한다. (가우시안 필터: 순환 대칭, 단일 돌출 필터)
# 3. sepFilter2D를 이용하여 img의 x, y를 각각의 kernel을 통하여 필터링한다.

ksize=(7,7)
gaussian_1d=cv2.getGaussianKernel(7,1.5) # 1차원 가우시안 계수 생성
gaussian_2d=np.outer(gaussian_1d,gaussian_1d.transpose())

gaussian_1dX=cv2.getGaussianKernel(ksize[0],1.5,cv2.CV_32F) # 가로 방향 마스크
gaussian_1dY=cv2.getGaussianKernel(ksize[1],1.5,cv2.CV_32F) # 세로 방향 마스크
gaussian_2d2=np.outer(gaussian_1dX,gaussian_1dY.transpose()) # 두 벡터의 외적

gauss_img1=cv2.filter2D(image,-1,gaussian_2d) # 사용자 생성 마스크 적용
gauss_img2=cv2.GaussianBlur(image,ksize,0) # OpenCV 제공 함수
gauss_img3=cv2.sepFilter2D(image,-1,gaussian_1dX,gaussian_1dY) # OpenCV 제공 함수 2

titles=['image','gauss_img1','gauss_img2','gauss_img3']
[cv2.imshow(t,eval(t))for t in titles]
cv2.waitKey(0)
