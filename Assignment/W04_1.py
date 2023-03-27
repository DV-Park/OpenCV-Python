import numpy as np, cv2

def onThreshold(value):
    th[0] = cv2.getTrackbarPos("Hue_th1", "result")
    th[1] = cv2.getTrackbarPos("Hue_th2", "result")
    _, result = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(result, th[0], 255, cv2.THRESH_BINARY, result)
    cv2.imshow("result", result)

#기본
BGR_img = cv2.imread("../Src/dog.jpg", cv2.IMREAD_COLOR)  # 컬러 영상 읽기
if BGR_img is None: raise Exception("영상 파일 읽기 오류")

white = np.array([255, 255, 255], np.uint8)
CMY_img = white - BGR_img
Cyan, Magenta, Yellow = cv2.split(CMY_img)  # 채널 분리

titles = ['BGR_img', 'CMY_img', 'Cyan', 'Magenta', 'Yellow']
[cv2.imshow(t, eval(t)) for t in titles]

#심화
BGR_img = cv2.imread("../Src/AppleTree.jpg", cv2.IMREAD_COLOR) # 컬러 영상 읽기
if BGR_img is None: raise Exception("영상 파일 읽기 오류")

HSV_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2HSV) # 컬러 공간 변환
hue = np.copy(HSV_img[:,:,0])                      # hue 행렬에 색상 채널 복사

th = [50, 100]                                     # 트랙바로 선택할 범위 변수
cv2.namedWindow("result")
cv2.createTrackbar("Hue_th1", "result", th[0], 255, onThreshold)
cv2.createTrackbar("Hue_th2", "result", th[1], 255, onThreshold)
onThreshold(th[0])                                 # 이진화 수행
cv2.imshow("BGR_img", BGR_img)
cv2.waitKey(0)
