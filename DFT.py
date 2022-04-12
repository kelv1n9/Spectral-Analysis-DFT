import numpy as np


def amp_filter(a, amp_slice):
    amp = a.copy()
    s = amp.shape[0]
    for n in range(len(amp)):
        if abs(amp[n]) / s < amp_slice:
            amp[n] = 0
    return amp


def dft(x):
    s = x.shape[0]
    x_k = np.zeros(s, dtype='complex_')

    for k in range(s):
        for n in range(s):
            x_k[k] += x[n] * np.exp(-2j * np.pi * n * k / s)
    return x_k


def ift(x):
    s = x.shape[0]
    x_n = np.zeros(s, dtype='complex_')

    for k in range(s):
        for n in range(s):
            x_n[k] += x[n] * np.exp(2j * np.pi * n * k / s)
    return x_n


def fft(x):
    s = x.shape[0]

    if s <= 32:
        return dft(x)
    else:
        left = fft(x[::2])
        right = fft(x[1::2])
        exp = np.exp(-2j * np.pi * np.arange(s) / s)
        return np.concatenate([left + exp[:int(s / 2)] * right, left + exp[int(s / 2):] * right])


def ifft(x):
    s = x.shape[0]

    if s <= 32:
        return ift(x)
    else:
        left = ifft(x[::2])
        right = ifft(x[1::2])
        exp = np.exp(2j * np.pi * np.arange(s) / s)
        return np.concatenate([left + exp[:int(s / 2)] * right, left + exp[int(s / 2):] * right])


def ft_freq(n, d):
    _freq = np.array([i / (d * n) for i in range(int(n / 2))])
    freq_ = np.array([i / (d * n) for i in range(int(-n / 2), 0)])
    return np.concatenate((_freq, freq_))
