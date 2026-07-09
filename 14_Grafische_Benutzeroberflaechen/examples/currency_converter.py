import tkinter as tk
from tkinter import ttk, messagebox

RATES = {'EUR':1.0, 'USD':1.1, 'GBP':0.85, 'TRY':53.0}

def convert(amount, frm, to):
    try:
        a = float(amount)
    except ValueError:
        return None
    eur = a / RATES.get(frm,1.0)
    return eur * RATES.get(to,1.0)

def main():
    root = tk.Tk()
    root.title('Währungsrechner (Demo)')

    frm = ttk.Frame(root, padding=10)
    frm.pack()

    ttk.Label(frm, text='Betrag').grid(row=0,column=0)
    amt = ttk.Entry(frm)
    amt.grid(row=0,column=1)

    ttk.Label(frm, text='Von').grid(row=1,column=0)
    from_cb = ttk.Combobox(frm, values=list(RATES.keys()))
    from_cb.current(0)
    from_cb.grid(row=1,column=1)

    ttk.Label(frm, text='Nach').grid(row=2,column=0)
    to_cb = ttk.Combobox(frm, values=list(RATES.keys()))
    to_cb.current(1)
    to_cb.grid(row=2,column=1)

    res_var = tk.StringVar()
    ttk.Label(frm, textvariable=res_var).grid(row=3,column=0,columnspan=2)

    def do():
        r = convert(amt.get(), from_cb.get(), to_cb.get())
        if r is None:
            messagebox.showerror('Fehler','Ungültiger Betrag')
        else:
            res_var.set(f'Resultat: {r:.2f} {to_cb.get()}')

    ttk.Button(frm, text='Konvertieren', command=do).grid(row=4,column=0,columnspan=2, pady=6)
    root.mainloop()

if __name__ == '__main__':
    main()
