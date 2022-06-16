import numpy as np
from scipy import signal

# perfusion indice
def sqi_perfusion_indice(filtered_signal, mean_raw_signal):
    """
    perfusion index is the gold standard for assessing PPG signal quality. pulsatile blood flow / nonpulsatile blood
    :param filtered_signal: filtered PPG signal
    :param mean_raw_signal: mean of the raw ppg signal
    :return: scalar, P_sqi
    """
    P_SQI = (np.max(filtered_signal) - np.min(filtered_signal)) / np.mean(mean_raw_signal) * 100
    return P_SQI


# skewness
# scipy.stats.skew

# kurtosis
# scipy.stats.kurtosis

# entropy
def sqi_entropy(signal):
    """

    :param signal:
    :return:
    """
    E_SQI = - np.sum(np.multiply(np.power(signal, 2), np.log(np.power(signal, 2))))
    return E_SQI


# zero crossing rate
def sqi_zero_crossing_num(signal):
    """

    :param signal:
    :return:
    """
    signal_size = len(signal)
    zero_crossing_num = 0
    for i in range(signal_size-2):
        if signal[i] * signal[i + 1] <= 0:
            zero_crossing_num += 1

    Z_SQI = zero_crossing_num / signal_size
    return Z_SQI


# signal-to-noise ratio
def sqi_signal_to_noise_ratio(filtered_signal):
    """

    :param filtered_signal:
    :return:
    """
    std_signal = np.std(np.abs(filtered_signal))
    std_noise = np.std(filtered_signal)
    N_SQI = std_signal / std_noise
    return N_SQI


# relative power, R_SQI
def sqi_relative_power(raw_signal):
    """

    :param signal:
    :return:
    """
    # remove mean
    raw_signal -= np.mean(raw_signal)

    # TODO: NFFT = max(256,2^nextpow2(length(Wave)));
    NFFT = np.max(256, 2 ** (np.ceil(np.log2(np.abs(raw_signal)))))
    Fs = 125

    # welch method
    f, pxx = signal.welch(x=raw_signal, window=len(signal), noverlap=len(signal) / 2, f=((NFFT*2)-1), fs=Fs)

    F1 = [1, 2.25]
    F2 = [0, 8]

    power_F1 = np.trapz(f[f >= F1[0] and f <= F1[0]], pxx[f >= F1[0] and f<= F1[0]])
    power_F2 = np.trapz(f[f >= F2[0] and f <= F2[0]], pxx[f >= F2[0] and f<= F2[0]])

    R_SQI = power_F1 / power_F2
    return R_SQI

