import numpy as np

x = np.array([7, -9, 6, -2, 10])
xf = np.fft.fft(x)

print(xf)

for i in xf:
    print(i)
    
