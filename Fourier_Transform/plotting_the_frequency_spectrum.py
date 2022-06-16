import numpy as np
import matplotlib.pyplot as plt

# x = np.loadtxt('../data/einthoven/ii.dat')
x = np.loadtxt('../data/augmented/avf.dat')

ecg = x[:, 1]
print(ecg.shape)
xf = np.fft.fft(ecg)
print(abs(xf).shape)

faxis = np.linspace(0, 200, len(xf))

plt.plot(faxis, abs(xf))
plt.show()