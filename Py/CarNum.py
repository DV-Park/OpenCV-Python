import cv2
# 배경과 이미지를 분리, 이미지마다 임계값이 다름
# Thresh_binary
# gray=cv2.imread("CarNum.jpg", cv2.IMREAD_GRAYSCALE)
# ret, dst=cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# Thresh_Triangle ??
src=cv2.imread("CarNum.jpg", cv2.IMREAD_GRAYSCALE)
gray=cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, dst=cv2.threshold(gray, 100, 255, cv2.THRESH_TRIANGLE)

cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()