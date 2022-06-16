import numpy as np
import math
import matplotlib.pyplot as plt

x = np.linspace(0, 2*math.pi, 200)

# flag = True
flag = False
if flag:
    wave_1 = np.cos(x * 2)

    plt.plot(wave_1)
    plt.xlabel("Angle")
    plt.ylabel("Amplitude")
    plt.title("An example of generating a waveform using a sinusoid")
    plt.show()

flag = True
# flag = False
if flag:
    wave_2 = np.cos(x * 3) + np.cos(x * 7 - 2)

    plt.plot(wave_2)
    plt.xlabel("Angle")
    plt.ylabel("Amplitude")
    plt.title("How to simulate PPG waveforms using sinusoids")
    plt.show()

