import numpy as np, cv2
from SrcCode.Common.filters import differential, filter

image = cv2.imread("../Src/CarNum.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

# 로버츠는 선명하지 않아 글자 구분이 잘 되지않는다.
# 프리윗은 선명하고 셋중에 엣지가 가장 잘 구분이 된다.
# 소벨은 선명하나 엣지가 두껍거나 좀 흐려서 프리윗보단 좋지 않다.

#로버츠
data1 = [-1, 0, 0,
          0, 1, 0,
          0, 0, 0]
data2 = [ 0, 0, -1,
          0, 1, 0,
          0, 0, 0]

#프리윗
data3 = [-1, 0, 1,                         # 프리윗 수직 마스크
         -1, 0, 1,
         -1, 0, 1]
data4 = [-1,-1,-1,                         # 프리윗 수평 마스크
          0, 0, 0,
          1, 1, 1]

#소벨
data5 = [-1, 0, 1,                  # 수직 마스크
         -2, 0, 2,
         -1, 0, 1]
data6 = [-1,-2,-1,                 # 수평 마스크
          0, 0, 0,
          1, 2, 1]

#로버츠
dst1 = cv2.filter2D(np.float32(image), -1, np.array(data1))
dst2 = cv2.filter2D(np.float32(image), -1, np.array(data2))

dst = cv2.magnitude(dst1,dst2)

#프리윗
pre, dst3, dst4 = differential(image, data3, data4)

#소벨
sob, dst5, dst6 = differential(image, data5, data6)

dst5 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, 3)  # x방향 미분 - 수직 마스크
dst6 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, 3)  # y방향 미분 - 수평 마스크

dst1=cv2.convertScaleAbs(dst1)
dst2=cv2.convertScaleAbs(dst2)
dst=cv2.convertScaleAbs(dst)

cv2.imshow("src: Image",image)
cv2.imshow("rob",dst)
cv2.imshow("pre",pre)
cv2.imshow("sob",sob)
cv2.waitKey(0)
cv2.destroyAllWindows()