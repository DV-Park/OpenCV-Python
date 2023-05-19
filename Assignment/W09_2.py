import matplotlib.pyplot as plt
import numpy as np

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

titles = ['1Hz (SINE)', '3Hz (SINE)', '5Hz (SINE)', '2Hz (COSINE)', '4Hz (COSINE)', '6Hz (COSINE)', '1Hz + 2Hz', '3Hz + 4Hz', '5Hz + 6Hz']
plt.figure(figsize=(13, 9))

# 원본 신호들 그리기
for i in range(6):
    plt.subplot(3, 3, i+1)
    plt.plot(t, g[i])
    plt.title(titles[i])

# 합성된 신호 그리기
plt.subplot(3, 3, 7)
plt.plot(t, g_sum1)
plt.title('1Hz + 2Hz')

plt.subplot(3, 3, 8)
plt.plot(t, g_sum2)
plt.title('3Hz + 4Hz')

plt.subplot(3, 3, 9)
plt.plot(t, g_sum3)
plt.title('5Hz + 6Hz')

plt.tight_layout()
plt.show()