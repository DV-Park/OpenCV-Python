import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        pt3,pt4=(x-60,y-40),(x+60,y+40)
        cv2.rectangle(image, pt3,pt4,blue,3,cv2.LINE_4)
        cv2.imshow(title1, image)

blue,green,red=(255,0,0),(0,255,0),(0,0,255)
image=np.zeros((400,600,3),np.uint8)
image[:]=(255,255,255)

pt1,pt2=(200,125),(400,275)

cv2.rectangle(image,pt1,pt2,blue,3,cv2.LINE_4)

title1='Rectangle'

cv2.imshow(title1, image)
cv2.setMouseCallback(title1, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()