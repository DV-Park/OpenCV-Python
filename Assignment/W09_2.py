import matplotlib.pyplot as plt
import numpy as np

t=np.arange(0,3,0.001)
g=[0]*5
g[0]=np.sin(2*np.pi*1*t)
g[1]=np.sin(2*np.pi*3*t)
g[2]=np.sin(2*np.pi*5*t)
g[3]=g[0]+g[1]+g[2]
g[4]=0.3*g[0]-0.7*g[1]+0.5*g[2]

titles=['1Hz','3Hz','5Hz','sum(1Hz+3Hz+5Hz)','weighted sum']
plt.figure(figsize=(13,6))
for i, title in enumerate(titles):
    plt.subplot(2,3,i+1)
    plt.plot(t,g[i])
    plt.title(title)
plt.tight_layout()
plt.show()