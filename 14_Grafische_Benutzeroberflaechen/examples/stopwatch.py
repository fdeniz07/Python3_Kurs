import tkinter as tk

class Stopwatch:
    def __init__(self, label):
        self._running = False
        self._time = 0
        self._label = label

    def _tick(self):
        if self._running:
            self._time += 1
            self._label.config(text=self._format(self._time))
            self._label.after(1000, self._tick)

    def _format(self, t):
        m, s = divmod(t, 60)
        return f'{m:02d}:{s:02d}'

    def start(self):
        if not self._running:
            self._running = True
            self._tick()

    def stop(self):
        self._running = False

    def reset(self):
        self._running = False
        self._time = 0
        self._label.config(text=self._format(self._time))

def main():
    root = tk.Tk()
    root.title('Stoppuhr')
    lbl = tk.Label(root, text='00:00', font=('Consolas', 24))
    lbl.pack(pady=10)
    sw = Stopwatch(lbl)

    frm = tk.Frame(root)
    frm.pack()
    tk.Button(frm, text='Start', command=sw.start).pack(side='left')
    tk.Button(frm, text='Stop', command=sw.stop).pack(side='left')
    tk.Button(frm, text='Reset', command=sw.reset).pack(side='left')
    root.mainloop()

if __name__ == '__main__':
    main()
