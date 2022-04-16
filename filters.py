import numpy as np


# Butterworth filter
def butter(freq, cutoff, n, type_):
    if type_ == "low":
        return 1 / np.sqrt(1 + np.power(freq / cutoff, 2 * n))
    if type_ == "high":
        return 1 / np.sqrt(1 + np.power(cutoff / freq, 2 * n))


# Amplitude filter
def amp_filter(a, amp_slice):
    amp = a.copy()
    s = amp.shape[0]
    for n in range(len(amp)):
        if abs(amp[n]) / s < amp_slice:
            amp[n] = 0
    return amp
