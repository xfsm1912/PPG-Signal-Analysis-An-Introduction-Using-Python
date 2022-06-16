import numpy as np
import math
import matplotlib.pyplot as plt

x = np.linspace(1, 100, 100)

# waveform of Gaussian function
# flag = True
flag = False
if flag:
    a = 1
    mu = 50
    sigma = 10

    y = a * np.exp(-((x-mu)/sigma)**2/2)
    plt.plot(x, y)
    plt.show()


# more than one gaussian function to formulate a waveform
# flag = True
flag = False
if flag:
    a = [0.8, 0.4]
    mu = [25, 50]
    sigma = [10, 20]

    y0 = a[0] * np.exp(-((x-mu[0])/sigma[0])**2/2)
    y1 = a[1] * np.exp(-((x-mu[1])/sigma[1])**2/2)
    y = y0 + y1

    plt.plot(x, y)
    plt.plot(x, y0, 'k--')
    plt.plot(x, y1, 'r--')
    plt.xlabel("Sampling points")
    plt.ylabel("Amplitude")
    plt.legend(["Synthetic PPG", "$1^{st}$ Gaussian", "$2^{nd}$ Gaussian"])
    plt.title("An example of generating a waveform using two Gaussian functions")
    plt.show()

# one PPG waveform after adding a circular motion
flag = True
# flag = False
if flag:
    Duration = 1
    Fs = 125 # Sampling Frequency
    a = [0.82, 0.4]
    mu = [-math.pi / 2, 0]
    sigma = [0.6, 1.2]

    Samples = Fs / Duration
    V_angle = 2 * math.pi / Samples
    angle = np.arange(-math.pi + V_angle, math.pi, V_angle)
    y0 = a[0] * np.exp(-((angle-mu[0])/sigma[0])**2/2)
    y1 = a[1] * np.exp(-((angle-mu[1])/sigma[0])**2/2)
    y = y0 + y1

    plt.plot(angle, y, 'b')
    plt.plot(angle, y0, 'k--')
    plt.plot(angle, y1, 'r--')
    plt.xlabel("Angle")
    plt.ylabel("Amplitude")
    plt.xlim([-math.pi, math.pi])
    plt.xticks([-math.pi, 0, math.pi], ['$\pi$', '0', '$\pi$'])
    plt.legend(["Synthetic PPG","$1^{st}$ Gaussian", "$2^{nd}$ Gaussian"])
    plt.title("An example of generating a waveform using angle model")
    plt.show()




