import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        pt3, pt4 = (x-60, y-40), (x+60, y+40)
        cv2.rectangle(image, pt3, pt4, blue, 3, cv2.LINE_4)
        cv2.imshow(title1, image)

image = cv2.imread("C:/Park/Src/dog.jpg")
if image is None: raise Exception("영상 파일 읽기 오류")

x, y = image.shape[1]//2, image.shape[0]//2
sx, sy = 100, 75

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)

pt1, pt2 = (x-sx, y-sy), (x+sx, y+sy)

cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4)

title1='Rectangle'

cv2.imshow(title1, image)
cv2.setMouseCallback(title1, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()