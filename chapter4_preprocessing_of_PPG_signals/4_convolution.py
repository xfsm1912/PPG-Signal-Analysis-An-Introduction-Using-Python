import numpy as np
import math
import os
import matplotlib.pyplot as plt
from scipy import signal

# Iplementing the moving average using a simple loop

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, "..", "data")
subfolder_dir = os.path.join(data_dir, "FINGERTIP_PPG_FROM_HYPERTENSIVE_SUBJECTS", "0_subject")

# load an fingertip data as example
ppg_data = np.loadtxt(os.path.join(subfolder_dir, "2_1.txt"))
ppg_data_size = len(ppg_data)


Duration = 1
Fs = 125  # Sampling Frequency
a = [0.82, 0.4]
mu = [-math.pi / 2, 0]
sigma = [0.6, 1.2]

Samples = Fs / Duration
V_angle = 2 * math.pi / Samples
angle = np.arange(-math.pi + V_angle, math.pi, V_angle)
y0 = a[0] * np.exp(-((angle - mu[0]) / sigma[0]) ** 2 / 2)
y1 = a[1] * np.exp(-((angle - mu[1]) / sigma[0]) ** 2 / 2)
y = y0 + y1

y_raw = y + np.random.normal(loc=0, scale=0.05, size=len(y))

# example 1: quality
# flag = True
flag = False
if flag:
    f = y
    # g = y_raw

    g = signal.resample(y_raw, len(f))

    conv_f_g = signal.convolve(f, g)
    conv_g_f = signal.convolve(g, f)

    fig, axs = plt.subplots(4, 1)
    fig.suptitle("Convolution")
    axs[0].plot(f, 'k-')
    axs[0].set_title('f: Template')
    axs[1].plot(g, 'r-')
    axs[1].set_title('g: raw signal')
    axs[2].plot(conv_f_g)
    axs[2].set_title('f * g')
    axs[3].plot(conv_g_f)
    axs[3].set_title('g * f')
    fig.tight_layout()
    plt.show()


# example 2: filtering PPG signal
flag = True
# flag = False
if flag:
    f = y
    g = ppg_data
    conv_f_g = signal.convolve(f, g)

    fig, axs = plt.subplots(3, 1)
    fig.suptitle("Convolution")
    axs[0].plot(f, 'k-')
    axs[0].set_title('f: Template')
    axs[1].plot(g, 'r-')
    axs[1].set_title('g: raw signal')
    axs[2].plot(conv_f_g)
    axs[2].set_title('f * g: filtered out ppg')
    fig.tight_layout()
    plt.show()

