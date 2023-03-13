import numpy as np
import cv2

image=cv2.imread("C:/Park/Src/dog.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

bn=100

switch_case = {
    ord('a') : "a키 입력",
    ord('b') : "b키 입력",
    0x41: "A키 입력",
    int('0x42', 16): "B키 입력",
    2424832: "왼쪽 화살표키 입력",
    2490368: "윗쪽 화살표키 입력",
    2555904: "오른쪽 화살표키 입력",
    2621440: "아래쪽 화살표키 입력"
}

image=np.ones((200,300), np.float64)
cv2.namedWindow("Keyboard Event")
cv2.imshow("Keyboard Event", image)

while True:
    key=cv2.waitKeyEx(100)
    if key ==  2490368: bn+=10
    elif key == 2621440: bn-=10
    elif key == ord('i') | ord('I') : bn=100
    elif key == 27: break
    try:
        result=switch_case[key]
        dst1 = cv2.add(image, bn)
        dst2 = cv2.subtract(image, bn)
        print(result)
    except KeyError:
        result=-1

cv2.destroyAllWindows()