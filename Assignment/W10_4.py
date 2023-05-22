import numpy as np, cv2, math
import scipy.fftpack as sf

block=np.zeros((8,8),np.uint8)
cv2.randn(block,128,50)

dct=cv2.dct(block.astype("float32"))
idct=cv2.dct(dct,flags=cv2.DCT_INVERSE)

print("Original block=\n", block)
print("dct(OpenCV 함수)=\n", dct)
print("idct(OpenCV 함수)=\n", cv2.convertScaleAbs(idct))