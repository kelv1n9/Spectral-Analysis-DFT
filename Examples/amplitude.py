import matplotlib.pyplot as plt
import numpy as np


def amp_filter(a, amp_slice):
    amp = a.copy()
    s = amp.shape[0]
    for n in range(len(amp)):
        if amp[n] < amp_slice:
            amp[n] = 0
    return amp


#plt.style.use('seaborn')

f = np.linspace(0, 100, 1000)
amps = np.abs(np.random.randn(*np.shape(f)))

plt.plot(f, amps, color='grey', label='Шум')
plt.plot(f, amp_filter(amps, 3), color='blue', label='Выделенный сигнал')
plt.hlines(3, 0, 100, color='red', linestyle='--', linewidth=2, label='Срез')
plt.legend(loc='upper left', shadow=True)
plt.show()
