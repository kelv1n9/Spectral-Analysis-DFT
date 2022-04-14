from Errors import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import AppBack
import matplotlib.pyplot as plt

"""
data = [a_ent, b_ent, f1_ent, f2_ent, amp_cut_ent, noise_amp_ent, df_ent, f_max_ent, r_btn, chk_btn, chk_btn2]
graph = [s_lx, s_rx, s_ly, s_ry, i_lx, i_rx, i_ly, i_ry]
ax = [ax1, ax2, ax3, ax4]
can = [canvas1, canvas2, canvas3, canvas4]
"""


class Root:
    def __init__(self):
        plt.style.use('dark_background')
        self.root = tk.Tk()
        self.window = tk.Toplevel(self.root)
        self.data, self.graph, self.ax, self.can, = [], [], [], []
        self.graph_temp, self.data_temp = [tk.Entry() for x in range(8)], [tk.Entry() for x in range(11)]
        self.log = tk.Label()

        self.root.bind_all('<Return>', (lambda event: self.btn_clk()))  # Забиндинные клавиши

        self.setup()

    def setup(self):
        self.root.minsize(320, 520)
        self.root.resizable(width=False, height=False)
        self.root.title("Окно конфигурации")

        self.window.minsize(800, 600)
        self.window.state('zoomed')  # Развернуть на весь экран
        self.window.columnconfigure([0, 1], minsize=50, weight=1)
        self.window.rowconfigure([0, 1], minsize=50, weight=1)
        self.window.title("Спектральный анализ")

    def make_root(self):
        group_1 = tk.LabelFrame(self.root, padx=15, pady=10, text="Функция")
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

        group_2 = tk.LabelFrame(self.root, padx=15, pady=10, text="Настройки")
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
        df_ent.insert(tk.END, '0.25')
        df_ent.grid(row=2, column=1, stick='nsew')
        tk.Label(group_2, text="Гц", font=("Arial", 10)).grid(row=2, column=2)
        tk.Label(group_2, text="Максимальная частота", font=("Arial", 10)).grid(row=3, column=0)
        f_max_ent = tk.Entry(group_2, width=5)
        f_max_ent.insert(tk.END, '128')
        f_max_ent.grid(row=3, column=1, stick='nsew')
        tk.Label(group_2, text="Гц", font=("Arial", 10)).grid(row=3, column=2)

        group_3 = tk.LabelFrame(self.root, padx=15, pady=10, text="Графики")
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
        s_ly_ent.insert(tk.END, '-5')
        s_ly_ent.grid(row=1, column=1, stick='nsew')
        tk.Label(group_3, text=" : ", font=("Arial", 10)).grid(row=1, column=2, stick='nsew')
        s_ry_ent = tk.Entry(group_3, width=5)
        s_ry_ent.insert(tk.END, '5')
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
        tk.Radiobutton(self.root, text='Fast Fourier Transform', variable=r_btn, value=1).place(x=10, y=355)
        tk.Radiobutton(self.root, text='Discrete Fourier Transform', variable=r_btn, value=2).place(x=150, y=355)

        chk_btn = tk.IntVar(value=0)
        chk_btn2 = tk.IntVar(value=0)
        tk.Checkbutton(self.root, text="Наложение входного и выходного сигнала", variable=chk_btn, onvalue=1,
                       offvalue=0).place(x=40, y=380)
        tk.Checkbutton(self.root, text="Показать линию среза", variable=chk_btn2, onvalue=1,
                       offvalue=0).place(x=40, y=400)

        self.log = tk.Label(self.root, text='')
        self.log.place(x=10, y=500)

        self.data_temp = [a_ent, b_ent, f1_ent, f2_ent, amp_cut_ent, noise_amp_ent, df_ent, f_max_ent, r_btn, chk_btn,
                          chk_btn2]
        self.graph_temp = [s_lx_ent, s_rx_ent, s_ly_ent, s_ry_ent, i_lx_ent, i_rx_ent, i_ly_ent, i_ry_ent]

        btn = tk.Button(self.root, command=self.btn_clk, text="Расчет", font=("Arial", 30))
        btn.place(x=10, y=420, width=300)

    def check_entry(self):
        data_ = [x.get() for x in self.data_temp]
        graph_data_ = [x.get() for x in self.graph_temp]

        for n in data_:
            if n == '':
                field_error()
                return
            else:
                self.data.append(float(n))

        for n in graph_data_:
            if n == '':
                field_error()
                return
            else:
                self.graph.append(float(n))

    def btn_clk(self):
        self.check_entry()
        # PAYLOAD
        bf = AppBack.AppBack(self.data)
        f, t = bf.signal()
        a, b, c, freq, time = bf.ft(f)

        self.draw(a, b, c, f, t, freq)

        self.log['text'] = '{:.3f} сек., {} точек'.format(time, t.shape[0])

    def make_window(self):
        titles = [['Source signal', 'Image'], ['Filtered image', 'Filtered signal']]
        for i in range(2):
            for j in range(2):
                frame = tk.Frame(self.window)
                frame.grid(row=i, column=j, stick='wens')

                fig = plt.Figure(figsize=(3, 3), dpi=100)
                axes = fig.add_subplot(111)
                axes.set_title(titles[i][j])

                canvas = FigureCanvasTkAgg(fig, master=frame)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                self.ax.append(axes)
                self.can.append(canvas)

    def draw(self, a, b, c, f, t, freq):
        [self.ax[x].clear() for x in range(4)]

        # Source signal
        self.ax[0].plot(t, f)
        self.ax[0].set_xlim(self.graph[0], self.graph[1])
        self.ax[0].set_ylim(self.graph[2], self.graph[3])
        self.ax[0].set_title('Source signal')
        self.ax[0].set_xlabel('Time, sec')
        self.ax[0].set_ylabel('Amplitude')
        self.can[0].draw()

        # Image
        self.ax[1].plot(freq, a)  # freq, np.abs(Unfiltered_s) / N
        self.ax[1].set_xlim(self.graph[4], self.graph[5])
        self.ax[1].set_ylim(self.graph[6], self.graph[7])
        self.ax[1].set_title('Image')
        self.ax[1].set_xlabel('Frequency, Hz')
        self.ax[1].set_ylabel('Amplitude/2')
        self.ax[1].grid(color='grey', linewidth=0.5, linestyle='--')
        if self.data[10] == 1:
            self.ax[1].hlines(self.data[4], self.graph[4], self.graph[5], color='red', linestyle='--', linewidth=2)
        self.can[1].draw()

        # Filtered Image
        self.ax[2].plot(freq, b)  # freq, np.abs(Filtered_i) / N
        self.ax[2].set_xlim(self.graph[4], self.graph[5])
        self.ax[2].set_ylim(self.graph[6], self.graph[7])
        self.ax[2].set_title('Filtered image')
        self.ax[2].set_xlabel('Frequency, Hz')
        self.ax[2].set_ylabel('Amplitude/2')
        self.ax[2].grid(color='grey', linewidth=0.5, linestyle='--')
        self.can[2].draw()

        # Filtered signal
        if self.data[9] == 1:
            self.ax[3].plot(t, f, label="Source signal")
            self.ax[3].plot(t, c, color='red', linewidth=3, label="Filtered signal")
            self.ax[3].set_title('Filtered and source signal')
            self.ax[3].legend()
        else:
            self.ax[3].plot(t, c)  # t, np.real(Filtered_s) / N
            self.ax[3].set_title('Filtered signal')

        self.ax[3].set_xlabel('Time, sec')
        self.ax[3].set_ylabel('Amplitude')
        self.ax[3].set_xlim(self.graph[0], self.graph[1])
        self.ax[3].set_ylim(self.graph[2], self.graph[3])
        self.can[3].draw()

        self.graph.clear()
        self.data.clear()


app = Root()
app.make_window()
app.make_root()
tk.mainloop()
