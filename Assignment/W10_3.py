import numpy as np

sig1=[4,5,6,2,8,10,20,9,4,5,3,4,15,12,20]
sig2=[8,10,20,9,4,5,3,4,15,12,20,4,5,6,2]

fft_sig1=np.fft.fft(sig1)
fft_sig2=np.fft.fft(sig2)
fft_sig2_conj=np.conj(fft_sig2)

R=(fft_sig1*fft_sig2_conj)/abs(fft_sig1*fft_sig2_conj)
r=np.fft.ifft(R)

time_shift=np.argmax(r)
print("time shift=%d"%(time_shift))