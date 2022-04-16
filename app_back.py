from DFT import fft, ift, dft, ifft, ft_freq
from Errors import degree_error, logger
from filters import amp_filter, butter
import numpy as np
import timeit

"""
data = [a_ent, b_ent, f1_ent, f2_ent, amp_cut_ent, freq_cut_ent, order, noise_amp_ent, 
                                                                df_ent, f_max_ent, r_btn, chk_btn, filter_btn] 13
"""


class AppBack:
    def __init__(self, data):
        self.a = data[0]
        self.b = data[1]
        self.f1 = data[2]
        self.f2 = data[3]
        self.amp_cutoff = data[4]
        self.freq_cutoff = data[5]
        self.order = data[6]
        self.noise_amp = data[7]
        self.df = data[8]
        self.f_max = data[9]
        self.radiobutton = data[10]
        self.filter_btn = data[12]

        self.n = int(2 * self.f_max / self.df)
        period = self.n / (2 * self.f_max)

        self.t = np.linspace(0, period, self.n)
        self.w = 2 * np.pi

    def signal(self, i=0):  # Исходный сигнал
        return self.t, self.a * np.sin(self.f1 * self.w * (self.t - 0.01 * i)) + self.b * np.cos(
            self.f2 * self.w * (self.t - 0.01 * i)) + self.noise()

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

            filtered_i = None

            # Отфильтрованные Амплитуды
            if self.filter_btn == 1:
                filtered_i = unfiltered_s * butter(freq, self.freq_cutoff, self.order, 'low')
            elif self.filter_btn == 2:
                filtered_i = unfiltered_s * butter(freq, self.freq_cutoff, self.order, 'high')
            elif self.filter_btn == 3:
                filtered_i = amp_filter(unfiltered_s, self.amp_cutoff)

            filtered_s = ifft(filtered_i)  # Отфильтрованный сигнал
            time = timeit.default_timer() - start_time

            return abs(unfiltered_s) / self.n, abs(filtered_i) / self.n, np.real(filtered_s) / self.n, freq, time

        if self.radiobutton == 2:
            start_time = timeit.default_timer()
            unfiltered_s = dft(f)  # Амплитуды
            freq = ft_freq(self.n, 1. / (2 * self.f_max))  # Частоты

            filtered_i = None

            if self.filter_btn == 1:
                filtered_i = unfiltered_s * butter(freq, self.freq_cutoff, self.order, 'low')
            elif self.filter_btn == 2:
                filtered_i = unfiltered_s * butter(freq, self.freq_cutoff, self.order, 'high')
            elif self.filter_btn == 3:
                filtered_i = amp_filter(unfiltered_s, self.amp_cutoff)

            filtered_s = ift(filtered_i)  # Отфильтрованный сигнал
            time = timeit.default_timer() - start_time

            return abs(unfiltered_s) / self.n, abs(filtered_i) / self.n, np.real(filtered_s) / self.n, freq, time
