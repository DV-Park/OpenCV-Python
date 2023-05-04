import cv2
import matplotlib.pyplot as plt

img=cv2.imread("../Src/dog.jpg")

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(img.shape)

hist=cv2.calcHist([img],[0],None,[256],[0,256])

plt.figure(figsize=(12,3))
plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
plt.plot(hist)
plt.show()