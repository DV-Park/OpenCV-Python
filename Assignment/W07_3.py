import cv2
import matplotlib.pyplot as plt

img1=cv2.imread("../Src/TestFlower2.jpg")

hist1=cv2.calcHist([img1],[0],None,[256],[0,256])
min=1

for i in range (15):
    fname = "../Src/flower{0:d}.jpg".format(i+1)
    img2 = cv2.imread(fname,cv2.IMREAD_COLOR)

    hist2=cv2.calcHist([img2],[0],None,[256],[0,256])

    corr1=cv2.compareHist(hist1,hist2,cv2.HISTCMP_CORREL)

    if(min>abs(corr1)) :
        min=abs(corr1)
        resultImg=img2
    cv2.imshow("test",resultImg)
    cv2.waitKey(0)

#fname = "../Src/flower{0:d}.jpg".format(minflower)
#print(fname)
print("가장 유사한 결과물입니다.")
result=cv2.imshow("result",resultImg)
cv2.waitKey(0)
cv2.destroyAllWindows()