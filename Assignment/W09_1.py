import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1, 0.001)
Hz = [1, 2, 10, 100]
amplitudes = [0.5, 1.5, 2.0]  # 변화시킬 진폭 값들
phases = [0, np.pi/4, np.pi/2]  # 변화시킬 위상 값들

# 여현파(COSINE) 신호 생성
signals = []
for amplitude in amplitudes:
    for phase in phases:
        g = amplitude * np.cos(2 * np.pi * Hz[0] * t + phase)  # 여현파(COSINE) 신호 생성
        signals.append(g)

plt.figure(figsize=(10, 10))
for i, signal in enumerate(signals):
    plt.subplot(3, 3, i+1)
    plt.plot(t, signal)
    plt.xlim(0, 1)
    plt.title("Amplitude: %.1f, Phase: %.2fπ" % (amplitudes[i//3], phases[i%3]/np.pi))

plt.tight_layout()
plt.show()