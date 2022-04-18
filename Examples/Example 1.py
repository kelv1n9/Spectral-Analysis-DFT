import numpy as np
import matplotlib.pyplot as plt
import timeit


def dft(x):
    s = x.shape[0]
    x_k = np.zeros(s, dtype='complex_')

    for k in range(s):
        for n in range(s):
            x_k[k] += x[n] * np.exp(-2j * np.pi * n * k / s)
    return x_k


def ft_freq(n, d):
    _freq = np.array([i / (d * n) for i in range(int(n / 2))])
    freq_ = np.array([i / (d * n) for i in range(int(-n / 2), 0)])
    return np.concatenate((_freq, freq_))


f_max = 32
f = 2 * f_max
df = 0.05
N = int(f / df)
T = N / f

t = np.linspace(0, T, N)
sin = np.sin(2 * np.pi * t)

freq = ft_freq(N, 1 / f)

start_time = timeit.default_timer()
amps = dft(sin)
time = timeit.default_timer() - start_time
print(time, N)

plt.style.use('seaborn')
plt.plot(freq, np.abs(amps) / N)
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда/2')
# plt.plot(t, sin)
plt.xlim(-6, 6)
plt.show()
