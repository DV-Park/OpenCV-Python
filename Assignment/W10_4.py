import numpy as np, cv2
from SrcCode.Common.dct2d import *

def dct2_mode(block, mode):
    if mode==1: return cv2.dct(block.astype('float32'))
    elif mode==2: return  cv2.dct(block.astype('float64'))

def idct2_mode(block, mode):
    if mode==1: return cv2.idct(block.astype('float32'))
    elif mode==2: return cv2.idct(block.astype('float64'))


def dct_filtering(img, filter, M, N):
    dst = np.empty(img.shape, np.float32)
    for i in range(0, img.shape[0], M):
        for j in range(0, img.shape[1], N):
            block = img[i:i+M, j:j+N]
            dct_block = dct2_mode(block, mode)
            dct_block = dct_block * filter
            dst[i:i+M, j:j+N] = idct2_mode(dct_block, mode)
    return cv2.convertScaleAbs(dst)

image = cv2.imread("../Src/dct.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일을 읽기 에러")
mode = 2
M, N = 8, 8
filters = [np.zeros((M, N), np.float32) for i in range(5)]
titles = ['DC Pass', 'High Pass', 'Low Pass', 'Vertical Pass', 'Horizental Pass' ]

filters[0][0, 0] = 1                        # DC 계수만 1 지정 – DC Pass
filters[1][:], filters[1][0, 0] = 1, 0      # 모든 계수 1, DC 계수만 0 지정 – High Pass
filters[2][:M//2, :N//2] = 1            # 저주파 영역 모두 1 지정 – Low Pass
filters[3][0, 1:] = 1                        # 첫 행열 1 지정 – Vertical
filters[4][1:, 0] = 1                  # 첫 열만 1 지정 – Horizental

for filter, title in zip(filters, titles):
    dst = dct_filtering(image, filter, M, N)          # ?? ??? DCT ??
    cv2.imshow(title, dst)

cv2.imshow("image", image)
cv2.waitKey(0)