import numpy as np
import os
import math
from scipy import signal
import matplotlib.pyplot as plt


def detect_peaks(PPG):
    return [500, 1000]

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

f = y
g = ppg_data
conv_f_g = signal.convolve(f, g)

# TODO: extract the smoothing wave part
s = conv_f_g

peakLocs = detect_peaks(s)

intervals = np.diff(peakLocs) / Fs


# interpolation
f_interpolation = 4
t = np.zeros(1, len((intervals)))

# TODO: finish codes in page 133
