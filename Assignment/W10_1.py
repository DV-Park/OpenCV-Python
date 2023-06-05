import numpy as np
import cv2
from SrcCode.Common.fft2d import fft2, ifft2, calc_spectrum, fftshift

def FFT(image, mode=2):
    if mode == 1:
        dft = fft2(image)
    elif mode == 2:
        dft = np.fft.fft2(image)
    elif mode == 3:
        dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft = fftshift(dft)  # 셔플링
    spectrum = calc_spectrum(dft)  # 주파수 스펙트럼 영상
    return dft, spectrum

def IFFT(dft, shape, mode=2):
    dft = fftshift(dft)  # 역 셔플링
    if mode == 1:
        img = ifft2(dft).real
    if mode == 2:
        img = np.fft.ifft2(dft).real
    if mode == 3:
        img = cv2.idft(dft, flags=cv2.DFT_SCALE)[:, :, 0]
    img = img[:shape[0], :shape[1]]  # 영삽입 부분 제거
    return cv2.convertScaleAbs(img)

image = cv2.imread('../Src/dft_240.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 에러")
cy, cx = np.divmod(image.shape, 2)[0]  # 행렬 중심점 구하기
mode = 1

dft, spectrum = FFT(image, mode)  # FFT 수행 및 셔플링

# Filter 1: Lowpass Filter with radius 30
lowpass_radius_1 = 30
lowpass_1 = np.zeros(dft.shape, np.float32)
cv2.circle(lowpass_1, (cx, cy), lowpass_radius_1, (1, 1), -1)
lowpassed_dft_1 = dft * lowpass_1
lowpassed_img_1 = IFFT(lowpassed_dft_1, image.shape, mode)

# Filter 2: Lowpass Filter with radius 60
lowpass_radius_2 = 60
lowpass_2 = np.zeros(dft.shape, np.float32)
cv2.circle(lowpass_2, (cx, cy), lowpass_radius_2, (1, 1), -1)
lowpassed_dft_2 = dft * lowpass_2
lowpassed_img_2 = IFFT(lowpassed_dft_2, image.shape, mode)

# Filter 3: Highpass Filter with radius 30
highpass_radius = 30
highpass = np.ones(dft.shape, np.float32)
cv2.circle(highpass, (cx, cy), highpass_radius, (0, 0), -1)
highpassed_dft = dft * highpass
highpassed_img = IFFT(highpassed_dft, image.shape, mode)

cv2.imshow("image", image)
cv2.imshow("lowpassed_img_1", lowpassed_img_1)
cv2.imshow("lowpassed_img_2", lowpassed_img_2)
cv2.imshow("highpassed_img", highpassed_img)
cv2.imshow("spectrum_img", spectrum)
cv2.imshow("lowpass_spect_1", calc_spectrum(lowpassed_dft_1))
cv2.imshow("lowpass_spect_2", calc_spectrum(lowpassed_dft_2))
cv2.imshow("highpass_spect", calc_spectrum(highpassed_dft))
cv2.waitKey(0)