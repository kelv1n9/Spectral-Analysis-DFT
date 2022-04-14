from DFT import fft, ift, dft, ifft, amp_filter, ft_freq
from Errors import degree_error, logger
import numpy as np
import timeit

"""
data = [a_ent, b_ent, f1_ent, f2_ent, amp_cut_ent, noise_amp_ent, df_ent, f_max_ent, r_btn, chk_btn, chk_btn2]
"""


class AppBack:
    def __init__(self, data):
        self.a = data[0]
        self.b = data[1]
        self.f1 = data[2]
        self.f2 = data[3]
        self.cutoff = data[4]
        self.noise_amp = data[5]
        self.df = data[6]
        self.f_max = data[7]
        self.radiobutton = data[8]

        self.n = int(2 * self.f_max / self.df)
        period = self.n / (2 * self.f_max)

        self.t = np.linspace(0, period, self.n)
        self.w = 2 * np.pi

    def signal(self):  # Исходный сигнал
        return self.a * np.sin(self.f1 * self.w * self.t) + self.b * np.cos(
            self.f2 * self.w * self.t) + self.noise(), self.t

    def noise(self):
        return self.noise_amp * 5 * np.random.randn(*np.shape(self.t))

    def ft(self, f):
        if self.radiobutton == 1:
            freq = ft_freq(self.n, 1. / (2 * self.f_max))  # Частоты

            if (self.n & (self.n - 1)) != 0:  # Проверка на степень двойки
                degree_error()
                logger.error("Размер вектора должен быть степенью двойки!")
                return np.zeros(self.n), np.zeros(self.n), np.zeros(self.n), freq, 0

            start_time = timeit.default_timer()
            unfiltered_s = fft(f)  # Амплитуды
            filtered_i = amp_filter(unfiltered_s, self.cutoff)  # Отфильтрованные Амплитуды
            filtered_s = ifft(filtered_i)  # Отфильтрованный сигнал
            time = timeit.default_timer() - start_time

            return abs(unfiltered_s) / self.n, abs(filtered_i) / self.n, np.real(filtered_s) / self.n, freq, time

        if self.radiobutton == 2:
            start_time = timeit.default_timer()
            unfiltered_s = dft(f)  # Амплитуды
            filtered_i = amp_filter(unfiltered_s, self.cutoff)  # Отфильтрованные Амплитуды
            filtered_s = ift(filtered_i)  # Отфильтрованный сигнал
            time = timeit.default_timer() - start_time

            freq = ft_freq(self.n, 1. / (2 * self.f_max))  # Частоты

            return abs(unfiltered_s) / self.n, abs(filtered_i) / self.n, np.real(filtered_s) / self.n, freq, time
