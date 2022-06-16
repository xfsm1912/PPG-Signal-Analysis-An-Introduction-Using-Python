import os
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal


# Iplementing the moving average using a simple loop

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, "..", "data")
subfolder_dir = os.path.join(data_dir, "FINGERTIP_PPG_FROM_HYPERTENSIVE_SUBJECTS", "0_subject")

# load an fingertip data as example
ppg_data = np.loadtxt(os.path.join(subfolder_dir, "2_1.txt"))
ppg_data_size = len(ppg_data)

# example 1: handmade smoothing
# flag = True
flag = False
if flag:
    window_size = 4
    raw_sig = ppg_data
    filtered_sig = np.zeros((ppg_data_size-window_size, ))

    for i in range(len(ppg_data)-window_size):
        filtered_sig[i] = 1 / window_size * (raw_sig[i] + raw_sig[i+1] + raw_sig[i+2] + raw_sig[i+3])

    plt.plot(raw_sig)
    plt.plot(filtered_sig)
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.title("Moving Average")
    plt.show()

# example 2: convoluion kernel for MA filter
# flag = True
flag = False
if flag:
    window_size = 4
    raw_sig = ppg_data
    kernel = [0, 0, 1/4, 1/4, 1/4, 1/4, 0, 0]
    filtered_sig = signal.convolve(raw_sig, kernel, mode='same')

    plt.plot(raw_sig)
    plt.plot(filtered_sig)
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.title("Moving Average")
    plt.show()


# example 3: Implementing the frequency response of Moving Average filter

flag = True
# flag = False
if flag:
    # sampling frequency in Hz
    Fs = 200
    window_size = 5
    num = (1 / window_size) * np.ones(window_size)
    dend = 1

    # Logarithimc scale
    L = np.logspace(0, 2)
    # call the frequency response function
    # older versions of SciPy, signal.signal.freqz doesn't have an option to return the frequencies in Hz, so you'll
    # have to scale the frequencies yourself afterwards.
    #
    # The equivalent of Matlab's
    #
    # [h, f] = freqz(b, a, n, fs)
    # using freqz from scipy.signal is:
    #
    # w, h = freqz(b, a, worN=n)
    # f = fs * w / (2*np.pi)
    # ref: https://stackoverflow.com/questions/29620694/matlab-freqz-function-in-python
    Z = signal.freqz(b=num, a=dend, worN=L, fs=Fs)
    # compute and display the magnitude response
    # since the return of Z in scipy is [w, h], so select the Z[1] to do absolute calculation
    plt.semilogx(L, np.abs(Z)[1], "k")
    plt.grid()
    plt.xlabel("Hz")
    plt.ylabel("Gain")
    plt.title("Moving Average")
    plt.show()


