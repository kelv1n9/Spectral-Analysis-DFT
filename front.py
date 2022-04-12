import tkinter as tk
from Errors import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def init():
    plt.style.use('dark_background')

    root = tk.Tk()
    root.minsize(320, 520)
    root.resizable(width=False, height=False)
    root.title("Окно конфигурации")

    window = tk.Toplevel(root)
    window.minsize(800, 600)
    window.state('zoomed')  # Развернуть на весь экран
    window.columnconfigure([0, 1], minsize=50, weight=1)
    window.rowconfigure([0, 1], minsize=50, weight=1)
    window.title("Спектральный анализ")

    return window, root


def make_root(root, func, lnc):
    group_1 = tk.LabelFrame(root, padx=15, pady=10, text="Функция")
    group_1.place(x=10, y=10, width=300, height=60)
    a_ent = tk.Entry(group_1, width=5)
    a_ent.grid(row=0, column=0, stick='nsew')
    tk.Label(group_1, text="Sin(", font=("Arial", 10)).grid(row=0, column=1)
    f1_ent = tk.Entry(group_1, width=5)
    f1_ent.grid(row=0, column=2, stick='nsew')
    tk.Label(group_1, text="wt) + ", font=("Arial", 10)).grid(row=0, column=3)
    b_ent = tk.Entry(group_1, width=5)
    b_ent.grid(row=0, column=4, stick='nsew')
    tk.Label(group_1, text="Cos(", font=("Arial", 10)).grid(row=0, column=5)
    f2_ent = tk.Entry(group_1, width=5)
    f2_ent.grid(row=0, column=6, stick='nsew')
    tk.Label(group_1, text="wt)", font=("Arial", 10)).grid(row=0, column=7)

    group_2 = tk.LabelFrame(root, padx=15, pady=10, text="Настройки")
    group_2.place(x=10, y=80, width=300)
    group_2.rowconfigure([0, 1, 2, 3], minsize=25, weight=1)
    group_2.columnconfigure([0, 1], minsize=25, weight=1)
    tk.Label(group_2, text="Уровень шума", font=("Arial", 10)).grid(row=0, column=0)
    noise_amp_ent = tk.Entry(group_2, width=5)
    noise_amp_ent.grid(row=0, column=1, stick='nsew')
    tk.Label(group_2, text="В", font=("Arial", 10)).grid(row=0, column=2)
    tk.Label(group_2, text="Амплитуда среза", font=("Arial", 10)).grid(row=1, column=0)
    amp_cut_ent = tk.Entry(group_2, width=5)
    amp_cut_ent.grid(row=1, column=1, stick='nsew')
    tk.Label(group_2, text="В", font=("Arial", 10)).grid(row=1, column=2)
    tk.Label(group_2, text="Шаг частоты", font=("Arial", 10)).grid(row=2, column=0)
    df_ent = tk.Entry(group_2, width=5)
    df_ent.grid(row=2, column=1, stick='nsew')
    tk.Label(group_2, text="Гц", font=("Arial", 10)).grid(row=2, column=2)
    tk.Label(group_2, text="Максимальная частота", font=("Arial", 10)).grid(row=3, column=0)
    f_max_ent = tk.Entry(group_2, width=5)
    f_max_ent.grid(row=3, column=1, stick='nsew')
    tk.Label(group_2, text="Гц", font=("Arial", 10)).grid(row=3, column=2)

    group_3 = tk.LabelFrame(root, padx=15, pady=10, text="Графики")
    group_3.place(x=10, y=225, width=300)
    group_3.rowconfigure([0, 1, 2, 3], minsize=1, weight=1)
    group_3.columnconfigure([0, 1, 2, 3], minsize=1, weight=1)
    tk.Label(group_3, text="Сигнал : Х ", font=("Arial", 10)).grid(row=0, column=0, stick='e')
    s_lx_ent = tk.Entry(group_3, width=5)
    s_lx_ent.insert(tk.END, '0')
    s_lx_ent.grid(row=0, column=1, stick='nsew')
    tk.Label(group_3, text=" : ", font=("Arial", 10)).grid(row=0, column=2, stick='nsew')
    s_rx_ent = tk.Entry(group_3, width=5)
    s_rx_ent.insert(tk.END, '1')
    s_rx_ent.grid(row=0, column=3, stick='nsew')
    tk.Label(group_3, text=" Y ", font=("Arial", 10)).grid(row=1, column=0, stick='e')
    s_ly_ent = tk.Entry(group_3, width=5)
    s_ly_ent.insert(tk.END, '-1')
    s_ly_ent.grid(row=1, column=1, stick='nsew')
    tk.Label(group_3, text=" : ", font=("Arial", 10)).grid(row=1, column=2, stick='nsew')
    s_ry_ent = tk.Entry(group_3, width=5)
    s_ry_ent.insert(tk.END, '1')
    s_ry_ent.grid(row=1, column=3, stick='nsew')

    tk.Label(group_3, text="Образ : Х ", font=("Arial", 10)).grid(row=2, column=0, stick='e')
    i_lx_ent = tk.Entry(group_3, width=5)
    i_lx_ent.insert(tk.END, '-16')
    i_lx_ent.grid(row=2, column=1, stick='nsew')
    tk.Label(group_3, text=" : ", font=("Arial", 10)).grid(row=2, column=2, stick='nsew')
    i_rx_ent = tk.Entry(group_3, width=5)
    i_rx_ent.insert(tk.END, '16')
    i_rx_ent.grid(row=2, column=3, stick='nsew')
    tk.Label(group_3, text=" Y ", font=("Arial", 10)).grid(row=3, column=0, stick='e')
    i_ly_ent = tk.Entry(group_3, width=5)
    i_ly_ent.insert(tk.END, '0')
    i_ly_ent.grid(row=3, column=1, stick='nsew')
    tk.Label(group_3, text=" : ", font=("Arial", 10)).grid(row=3, column=2, stick='nsew')
    i_ry_ent = tk.Entry(group_3, width=5)
    i_ry_ent.insert(tk.END, '1')
    i_ry_ent.grid(row=3, column=3, stick='nsew')

    r_btn = tk.IntVar(value=1)
    tk.Radiobutton(root, text='Fast Fourier Transform', variable=r_btn, value=1).place(x=10, y=355)
    tk.Radiobutton(root, text='Discrete Fourier Transform', variable=r_btn, value=2).place(x=150, y=355)

    chk_btn = tk.IntVar(value=0)
    chk_btn2 = tk.IntVar(value=0)
    tk.Checkbutton(root, text="Наложение входного и выходного сигнала", variable=chk_btn, onvalue=1,
                   offvalue=0).place(x=40, y=380)
    tk.Checkbutton(root, text="Показать линию среза", variable=chk_btn2, onvalue=1,
                   offvalue=0).place(x=40, y=400)

    def btn_click():
        a = a_ent.get()
        b = b_ent.get()
        f1 = f1_ent.get()
        f2 = f2_ent.get()
        amp = amp_cut_ent.get()
        noise = noise_amp_ent.get()
        df = df_ent.get()
        f_max = f_max_ent.get()

        s_rx = s_rx_ent.get()
        s_lx = s_lx_ent.get()
        s_ry = s_ry_ent.get()
        s_ly = s_ly_ent.get()

        i_rx = i_rx_ent.get()
        i_lx = i_lx_ent.get()
        i_ry = i_ry_ent.get()
        i_ly = i_ly_ent.get()

        data = [a, b, f1, f2, amp, noise, df, f_max, s_lx, s_rx, s_ly, s_ry, i_lx, i_rx, i_ly, i_ry]
        int_data = []
        for n in data:
            if n == '':
                field_error()
                return
            else:
                int_data.append(float(n))

        func(int_data, lnc, r_btn.get(), chk_btn.get(), chk_btn2.get())

    def enter(event):
        btn_click()

    btn = tk.Button(root, command=btn_click, text="Расчет", font=("Arial", 30))
    root.bind_all('<Return>', enter)
    btn.place(x=10, y=420, width=300)


def make_window(window):
    ax, can = [], []
    titles = [['Source signal', 'Image'], ['Filtered image', 'Filtered signal']]
    for i in range(2):
        for j in range(2):
            frame = tk.Frame(window)
            frame.grid(row=i, column=j, stick='wens')

            fig = plt.Figure(figsize=(3, 3), dpi=100)
            axes = fig.add_subplot(111)
            axes.set_title(titles[i][j])

            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            ax.append(axes)
            can.append(canvas)

    return ax + can
