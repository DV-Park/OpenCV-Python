import cv2
import matplotlib.pyplot as plt
import pywt
import matplotlib.pyplot as plt

src=cv2.imread("../Src/filter.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

titles=['Approximation','Horizontal detail', 'Vertical detail', 'Diagonal detail']
coeffs2 = pywt.dwt2(src, wavelet='haar')

LL,(LH,HL,HH)=coeffs2
fig=plt.figure(figsize=(12,3))
for i, a in enumerate([LL,LH,HL,HH]):
    ax=fig.add_subplot(1,4,i+1)
    ax.imshow(a,interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i],fontsize=10)
plt.show()
cv2.destroyAllWindows()