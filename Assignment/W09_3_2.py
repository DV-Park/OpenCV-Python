import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 3, 0.001)
g = [0] * 6

# 정현파(SINE) 신호 생성
g[0] = np.sin(2 * np.pi * 1 * t)
g[1] = np.sin(2 * np.pi * 3 * t)
g[2] = np.sin(2 * np.pi * 5 * t)

# 여현파(COSINE) 신호 생성
g[3] = np.cos(2 * np.pi * 2 * t)
g[4] = np.cos(2 * np.pi * 4 * t)
g[5] = np.cos(2 * np.pi * 6 * t)

# 여현파와 정현파를 합성한 신호 생성
g_sum1 = g[0] + g[3]
g_sum2 = g[1] + g[4]
g_sum3 = g[2] + g[5]

N = len(t)
fmax = 1 / (t[1] - t[0])
xf_sum1 = np.fft.fft(g_sum1) / N
xf_sum2 = np.fft.fft(g_sum2) / N
xf_sum3 = np.fft.fft(g_sum3) / N
f = np.fft.fftfreq(N, 1 / fmax)

plt.figure(figsize=(8, 8))
plt.subplot(3, 1, 1)
plt.plot(f, np.abs(xf_sum1))
plt.title('Frequency Spectrum (Sum 1)')

plt.subplot(3, 1, 2)
plt.plot(f, np.abs(xf_sum2))
plt.title('Frequency Spectrum (Sum 2)')

plt.subplot(3, 1, 3)
plt.plot(f, np.abs(xf_sum3))
plt.title('Frequency Spectrum (Sum 3)')

plt.tight_layout()
plt.show()

# 주파수 계수 출력
print("Sum 1:")
for i, val in enumerate(np.abs(xf_sum1)):
    print(f'주파수 {f[i]:.2f} Hz의 계수: {val}')

print("\nSum 2:")
for i, val in enumerate(np.abs(xf_sum2)):
    print(f'주파수 {f[i]:.2f} Hz의 계수: {val}')

print("\nSum 3:")
for i, val in enumerate(np.abs(xf_sum3)):
    print(f'주파수 {f[i]:.2f} Hz의 계수: {val}')