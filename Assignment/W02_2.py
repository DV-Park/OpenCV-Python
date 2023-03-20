import numpy as np
import cv2

image=cv2.imread("C:/Park/Src/dog.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

bn=0

switch_case = {
    ord('i') : "i키 입력",
    ord('I') : "I키 입력",
    2490368: "윗쪽 화살표키 입력",
    2621440: "아래쪽 화살표키 입력"
}

cv2.imshow("Keyboard Event", image)

while True:
    key=cv2.waitKeyEx(100)
    if key ==  2490368: bn+=10
    elif key == 2621440: bn-=10
    elif key == ord('i') : bn=0
    elif key == ord('I'): bn =0
    elif key == 27: break
    try:
        result=switch_case[key]
        dst1 = cv2.add(image, bn)
        cv2.imshow("Keyboard Event", dst1)
        print(result)
    except KeyError:
        result=-1

cv2.destroyAllWindows()