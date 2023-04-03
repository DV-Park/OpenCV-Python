import numpy as np,cv2

def salt_pepper_noise(img, n):
    h, w = img.shape[:2]
    x, y = np.random.randint(0, w, n), np.random.randint(0, h, n)
    noise = img.copy()
    for (x,y) in zip(x,y):
        noise[y, x] = 0 if np.random.rand() < 0.5 else 255
    return noise

image = cv2.imread("../Src/CarNum.jpg")
if image is None: raise Exception("영상 파일 읽기 오류")

noise = salt_pepper_noise(image,500)
cv2.imwrite("noise.jpg",noise)
med_img=cv2.medianBlur(noise,3)

cv2.imshow("image",image)
cv2.imshow("noise",noise)
cv2.imshow("median Filtering",med_img)
cv2.waitKey(0)
