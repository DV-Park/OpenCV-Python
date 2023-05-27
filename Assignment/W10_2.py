import numpy as np
import cv2
from SrcCode.Common.fft2d import FFT, IFFT, calc_spectrum
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_gaussianFilter(shape, R):
    u = np.array(shape) // 2
    y = np.arange(-u[0], u[0], 1)
    x = np.arange(-u[1], u[1], 1)
    x, y = np.meshgrid(x, y)
    filter = np.exp(-(x**2 + y**2) / (2 * R**2))
    return x, y, filter if len(shape) < 3 else cv2.merge([filter, filter])

def get_butterworthFilter(shape, R, n):
    u = np.array(shape) // 2
    y = np.arange(-u[0], u[0], 1)
    x = np.arange(-u[1], u[1], 1)
    x, y = np.meshgrid(x, y)
    dist = np.sqrt(x**2 + y**2)
    filter = 1 / (1 + np.power(dist / R, 2 * n))
    return x, y, filter if len(shape) < 3 else cv2.merge([filter, filter])

image = cv2.imread('../Src/filter.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 에러")

mode = 3
dft, spectrum = FFT(image, mode)
x1, y1, gauss_filter = get_gaussianFilter(dft.shape, 30)
x2, y2, butter_filter = get_gaussianFilter(dft.shape, 60)

filtered_dft1 = dft * gauss_filter
filtered_dft2 = dft * butter_filter
gauss_img = IFFT(filtered_dft1, image.shape, mode)
butter_img = IFFT(filtered_dft2, image.shape, mode)
spectrum1 = calc_spectrum(filtered_dft1)
spectrum2 = calc_spectrum(filtered_dft2)

if mode == 3:
    gauss_filter, butter_filter = gauss_filter[:, :, 0], butter_filter[:, :, 0]

fig = plt.figure(figsize=(10, 10))
ax1 = plt.subplot(332, projection='3d')
ax1.plot_surface(x1, y1, gauss_filter, cmap='RdPu')
plt.title('Gaussian Filter (Radius 30)')
ax2 = plt.subplot(333, projection='3d')
ax2.plot_surface(x2, y2, butter_filter, cmap='RdPu')
plt.title('Gaussian Filter (Radius 60)')

titles = ['Input Image', 'Gaussian (Radius 30)', 'Gaussian (Radius 60)',
          'Input Spectrum', 'Gaussian Spectrum (Radius 30)', 'Gaussian Spectrum (Radius 60)']
images = [image, gauss_img, butter_img, spectrum, spectrum1, spectrum2]
plt.gray()
for i, t in enumerate(titles):
    plt.subplot(3, 3, i + 4)
    plt.imshow(images[i])
    plt.title(t)
plt.tight_layout()
plt.show()