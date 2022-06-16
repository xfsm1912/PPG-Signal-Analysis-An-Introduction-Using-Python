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

# example 1: a butter of order m
# implementing the frequency response of Butterworth filter
# flag = True
flag = False
if flag:
    Fs = 200
    Fc = 6 / (Fs / 2)
    m = 6
    # Butterworth filter
    num, dend = signal.butter(m, Fc)
    # Logarithimc scale
    L = np.logspace(0, 2)
    # call the Frequency response function
    # remember to set up the parameter for fs, because the signal.freqz's parameter order is different from Matlab
    Z = signal.freqz(b=num, a=dend, worN=L, fs=Fs)
    plt.semilogx(L, np.abs(Z)[1], "k")
    plt.grid()
    plt.xlabel("Hz")
    plt.ylabel("Gain")
    plt.title("Butterworth")
    plt.show()

# example 2: Cheby I
# flag = True
flag = False
if flag:
    Fs = 200
    Fc = 6 / (Fs / 2)
    m = 6
    Rs = 18
    # Butterworth filter
    num, dend = signal.cheby1(m, Rs, Fc)
    # Logarithimc scale
    L = np.logspace(0, 2)
    # call the Frequency response function
    Z = signal.freqz(b=num, a=dend, worN=L, fs=Fs)
    plt.semilogx(L, np.abs(Z)[1], "k")
    plt.grid()
    plt.xlabel("Hz")
    plt.ylabel("Gain")
    plt.title("Chebyshev 1")
    plt.show()

# example 3: Cheby II
# flag = True
flag = False
if flag:
    Fs = 200
    Fc = 6 / (Fs / 2)
    m = 6
    Rs = 18
    # Butterworth filter
    num, dend = signal.cheby2(m, Rs, Fc)
    # Logarithimc scale
    L = np.logspace(0, 2)
    # call the Frequency response function
    Z = signal.freqz(b=num, a=dend, worN=L, fs=Fs)
    plt.semilogx(L, np.abs(Z)[1], "k")
    plt.grid()
    plt.xlabel("Hz")
    plt.ylabel("Gain")
    plt.title("Chebyshev 2")
    plt.show()


# example 4: Elliptic filter
flag = True
# flag = False
if flag:
    Fs = 200
    Fc = 6 / (Fs / 2)
    m = 6
    Rp = 0.5
    Rc = 20
    # Butterworth filter
    num, dend = signal.ellip(m, Rp, Rc, Fc)
    # Logarithimc scale
    L = np.logspace(0, 2)
    # call the Frequency response function
    Z = signal.freqz(b=num, a=dend, worN=L, fs=Fs)
    plt.semilogx(L, np.abs(Z)[1], "k")
    plt.grid()
    plt.xlabel("Hz")
    plt.ylabel("Gain")
    plt.title("Elliptic")
    plt.show()

