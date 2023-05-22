import numpy as np
import cv2

src=cv2.imread("../Src/dft_256.jpg")
cv2.imshow("Original",src)

t_mat=np.array([[1,0,100],[0,1,-50]], dtype=np.float32)
dst=cv2.warpAffine(src,t_mat,dsize=(0,0))
cv2.imshow("Translation", dst)

src=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
dst=cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)

src=np.float32(src)
dst=np.float32(dst)
ret=cv2.phaseCorrelate(src,dst)
print(ret)

#추가한것
fft_src=np.fft.fft(src)
fft_dst=np.fft.fft(dst)
fft_dst_conj=np.conj(fft_dst)

R=(fft_src*fft_dst_conj)/abs(fft_src*fft_dst_conj)
r=np.fft.ifft(R)

cv2.waitKey(0)
cv2.destroyAllWindows()
time_shift=np.argmax(r)
print("Time shift=%d" % (time_shift))