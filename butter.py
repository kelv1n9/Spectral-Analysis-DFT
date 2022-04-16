import numpy as np
import matplotlib.pyplot as plt


def butter(freq, cutoff, n, type_):
    if type_ == "low":
        return 1 / np.sqrt(1 + np.power(freq / cutoff, 2 * n))
    if type_ == "high":
        return 1 / np.sqrt(1 + np.power(cutoff / freq, 2 * n))


f = np.linspace(0, 1000, 1000)
amp = np.array([1 for i in range(1000)])
amp1 = amp * butter(f, 100, 2, 'low')

plt.style.use('dark_background')
plt.plot(f, amp)
plt.plot(f, 20 * np.log10(amp1 / amp))
plt.plot(100, 20 * np.log10(np.sqrt(1 / 2)), marker='o')
plt.xscale('log')
plt.grid(color='grey', linewidth=0.5, linestyle='--')
plt.show()
