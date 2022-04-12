from DFT import *
from Errors import *
import timeit


def noise(t, noise_amp):
    return noise_amp * 5 * np.random.randn(*np.shape(t))


def signal(a1, a2, f1, f2, f_max, df, noise_amp):  # Исходный сигнал
    f_s = 2 * f_max  # Теорема Котельникова - Шеннона
    n = int(f_s / df)
    period = n / f_s

    t = np.linspace(0, period, n)
    w = 2 * np.pi
    return a1 * np.sin(f1 * w * t) + a2 * np.cos(f2 * w * t) + noise(t, noise_amp), t


def back_func(amp_slice, f_max, df, f, r_btn):
    f_s = 2 * f_max  # Теорема Котельникова - Шеннона
    n = int(f_s / df)
    period = n / f_s

    if r_btn == 1:
        freq = ft_freq(n, 1. / f_s)  # Частоты

        if (n & (n - 1)) != 0:  # Проверка на степень двойки
            degree_error()
            logger.error("Размер вектора должен быть степенью двойки!")
            return np.zeros(n), np.zeros(n), np.zeros(n), freq, 0

        start_time = timeit.default_timer()
        unfiltered_s = fft(f)  # Амплитуды
        filtered_i = amp_filter(unfiltered_s, amp_slice)  # Отфильтрованные Амплитуды
        filtered_s = ifft(filtered_i)  # Отфильтрованный сигнал
        time = timeit.default_timer() - start_time

        return abs(unfiltered_s) / n, abs(filtered_i) / n, np.real(filtered_s) / n, freq, time

    if r_btn == 2:
        start_time = timeit.default_timer()
        unfiltered_s = dft(f)  # Амплитуды
        filtered_i = amp_filter(unfiltered_s, amp_slice)  # Отфильтрованные Амплитуды
        filtered_s = ift(filtered_i)  # Отфильтрованный сигнал
        time = timeit.default_timer() - start_time

        freq = ft_freq(n, 1. / f_s)  # Частоты

        return abs(unfiltered_s) / n, abs(filtered_i) / n, np.real(filtered_s) / n, freq, time
