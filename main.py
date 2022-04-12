from back import *
from front import *


# data = [a, b, f1, f2, cutoff, noise, df, f_max, s_lx, s_rx, s_ly, s_ry, i_lx, i_rx, i_ly, i_ry]
def func(data, lnc_, r_btn_, chk_btn_, chk_btn2_):
    f, t = signal(data[0], data[1], data[2], data[3], data[7], data[6], data[5])
    [lnc_[x].clear() for x in range(4)]

    lnc_[0].plot(t, f)
    lnc_[0].set_xlim(data[8], data[9])
    lnc_[0].set_ylim(data[10], data[11])
    lnc_[0].set_title('Source signal')
    lnc_[0].set_xlabel('Time, sec')
    lnc_[0].set_ylabel('Amplitude')
    lnc_[4].draw()

    a, b, c, freq, time = back_func(data[4], data[7], data[6], f, r_btn_)

    lnc_[1].plot(freq, a)  # freq, np.abs(Unfiltered_s) / N
    lnc_[1].set_xlim(data[12], data[13])
    lnc_[1].set_ylim(data[14], data[15])
    lnc_[1].set_title('Image')
    lnc_[1].set_xlabel('Frequency, Hz')
    lnc_[1].set_ylabel('Amplitude/2')
    if chk_btn2_ == 1:
        lnc_[1].hlines(data[4], data[12], data[13], color='red', linestyle='--', linewidth=2)
    lnc_[5].draw()

    lnc_[2].plot(freq, b)  # freq, np.abs(Filtered_i) / N
    lnc_[2].set_xlim(data[12], data[13])
    lnc_[2].set_ylim(data[14], data[15])
    lnc_[2].set_title('Filtered image')
    lnc_[2].set_xlabel('Frequency, Hz')
    lnc_[2].set_ylabel('Amplitude/2')
    lnc_[6].draw()

    if chk_btn_ == 1:
        lnc_[3].plot(t, f, label="Source signal")
        lnc_[3].plot(t, c, color='red', linewidth=3, label="Filtered signal")
        lnc_[3].set_title('Filtered and source signal')
        lnc_[3].legend()
    else:
        lnc_[3].plot(t, c)  # t, np.real(Filtered_s) / N
        lnc_[3].set_title('Filtered signal')

    lnc_[3].set_xlabel('Time, sec')
    lnc_[3].set_ylabel('Amplitude')
    lnc_[3].set_xlim(data[8], data[9])
    lnc_[3].set_ylim(data[10], data[11])
    lnc_[7].draw()

    tk.Label(root, text='{:.3f} сек., {} точек'.format(time, t.shape[0])).place(x=10, y=500)


window, root = init()
lnc = make_window(window)
make_root(root, func, lnc)

window.mainloop()
