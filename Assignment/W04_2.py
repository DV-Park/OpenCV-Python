import numpy as np, cv2

img=cv2.imread("../Src/CarNum.jpg", cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception("영상 파일 읽기 오류")


# 필터의 크기가 커질수록 블러링이 강해진다.

#data =[1/9 for i in range(9)]
#data =[1/25 for i in range(25)]
data =[1/81 for i in range(81)]

#mask =np.array(data,np.float32).reshape(3,3)
#mask =np.array(data,np.float32).reshape(5,5)
mask =np.array(data,np.float32).reshape(9,9)

blur_img=cv2.filter2D(img,-1,mask)
dst=cv2.vconcat([img,blur_img])
cv2.imshow("bluring",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()