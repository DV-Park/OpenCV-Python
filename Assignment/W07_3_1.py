import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("../Src/TestFlower2.jpg")
img1_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
img1_hsv_hist = cv2.calcHist([img1_hsv],[0],None,[256],[0,256])

min_diff = float('inf')
result_img = None

for i in range (15):
    fname = "../Src/flower{0:d}.jpg".format(i+1)
    img2 = cv2.imread(fname,cv2.IMREAD_COLOR)
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    img2_hsv = cv2.cvtColor(img2_resized, cv2.COLOR_BGR2HSV)
    img2_hsv_hist = cv2.calcHist([img2_hsv],[0],None,[256],[0,256])

    diff = cv2.compareHist(img1_hsv_hist, img2_hsv_hist, cv2.HISTCMP_CHISQR)

    if(diff < min_diff):
        min_diff = diff
        result_img = img2_resized

cv2.imshow("result", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()