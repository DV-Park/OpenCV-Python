import cv2

#cv로 하는게 더 잘나옴

image=cv2.imread("dog.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

dst1=cv2.add(image,100)
dst2=cv2.subtract(image,100)

dst3=image+100
dst4=image-100

cv2.imshow("original image",image)
cv2.imshow("dst1-bright:opencv",dst1)
cv2.imshow("dst2-dark:opencv",dst2)
cv2.imshow("dst3-bright:numpy",dst3)
cv2.imshow("dst4-dark:numpy",dst4)
cv2.waitKey(0)