import numpy as np
import cv2

src = cv2.imread("../Src/dft_256.jpg")
cv2.imshow("Original", src)

t_mat = np.array([[1, 0, 100], [0, 1, -50]], dtype=np.float32)
dst = cv2.warpAffine(src, t_mat, dsize=(0, 0))
cv2.imshow("Translation", dst)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

src_gray = np.float32(src_gray)
dst_gray = np.float32(dst_gray)
ret = cv2.phaseCorrelate(src_gray, dst_gray)
print(ret)

# 위상 상관 결과에서 이동 거리 계산
shift_x, shift_y = ret[0]
rows, cols = src_gray.shape
dx = shift_x if shift_x <= rows / 2 else shift_x - rows
dy = shift_y if shift_y <= cols / 2 else shift_y - cols
print("이동 거리 (dx, dy):", (dx, dy))

# 추가한 부분
fft_src = np.fft.fft2(src_gray)
fft_dst = np.fft.fft2(dst_gray)
fft_dst_conj = np.conj(fft_dst)

R = (fft_src * fft_dst_conj) / np.abs(fft_src * fft_dst_conj)
r = np.fft.ifft2(R)

time_shift = np.argmax(r)
print("시간 이동 거리:", time_shift)

cv2.waitKey(0)
cv2.destroyAllWindows()