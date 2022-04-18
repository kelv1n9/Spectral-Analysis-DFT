import numpy as np
import matplotlib.pyplot as plt


def butter(freq, cutoff, n, type_):
    if type_ == "low":
        return 1 / np.sqrt(1 + np.power(freq / cutoff, 2 * n))
    if type_ == "high":
        return 1 / np.sqrt(1 + np.power(cutoff / freq, 2 * n))


plt.style.use('seaborn')

f = np.linspace(0, 1000000, 1000000)
amp = np.array([1 for i in range(1000000)])
amp1 = amp * butter(f, 1000, 1, 'low')

plt.plot(f, 20 * np.log10(amp1 / amp))

plt.xlabel('Частота (Гц)')
plt.ylabel('Ослабление (дБ)')
plt.legend()
plt.xscale('log')
plt.plot(1000, 20 * np.log10(np.sqrt(1 / 2)), marker='o')
plt.grid(color='grey', linewidth=0.5, linestyle='--')
plt.show()
