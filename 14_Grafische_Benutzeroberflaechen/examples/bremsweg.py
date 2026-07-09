import tkinter as tk
from tkinter import ttk, messagebox

def calc(v, a):
    # einfache Näherung: bremsweg = v^2 / (2*a)
    try:
        v = float(v)
        a = float(a)
        if a <= 0:
            return None
        return v*v / (2*a)
    except Exception:
        return None

def main():
    root = tk.Tk()
    root.title('Bremsweg-Rechner')

    frm = ttk.Frame(root, padding=10)
    frm.pack()

    ttk.Label(frm, text='Geschwindigkeit (m/s)').grid(row=0,column=0)
    v = ttk.Entry(frm) 
    v.grid(row=0,column=1) 

    ttk.Label(frm, text='Bremsverzögerung (m/s²)').grid(row=1,column=0) 
    a = ttk.Entry(frm)
    a.grid(row=1,column=1)

    res = tk.StringVar()
    ttk.Label(frm, textvariable=res).grid(row=2,column=0,columnspan=2)

    def do():
        r = calc(v.get(), a.get())
        if r is None:
            messagebox.showerror('Fehler','Ungültige Eingabe')
        else:
            res.set(f'Bremsweg ≈ {r:.2f} m')

    ttk.Button(frm, text='Berechnen', command=do).grid(row=3,column=0,columnspan=2, pady=6)
    root.mainloop()

if __name__ == '__main__':
    main()
