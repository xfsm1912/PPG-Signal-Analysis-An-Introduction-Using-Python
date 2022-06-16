import numpy as np
import matplotlib.pyplot as plt

# x = np.loadtxt('../data/einthoven/iii.dat')
x = np.loadtxt('../data/augmented/avf.dat')

ecg = x[:, 1]
print(ecg.shape)
xf = np.fft.fft(ecg)
print(abs(xf).shape)

faxis = np.linspace(0, 200, len(xf))

# remove 10Hz noise
k1 = int(len(xf) / 200 * 5)
k2 = int(len(xf) / 200 * 15)

xf[k1:k2+1] = 0
xf[len(xf) - k2:len(xf) - k1+1] = 0

# inverse fft
ecg_clean = np.fft.ifft(xf)

ecg_clean = np.real(ecg_clean)

# plt.plot(faxis, abs(xf))
plt.plot(ecg)
plt.plot(ecg_clean)
plt.show()



