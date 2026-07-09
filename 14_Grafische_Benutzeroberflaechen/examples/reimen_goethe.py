import random
import tkinter as tk

GOETHE_LINES = [
    "Über allen Gipfeln ist Ruh'",
    "Die Nacht ist gekommen",
    "Wer nie sein Brot mit Tränen aß",
    "Ein guter Mensch in seinem dunklen Drange",
    "Faust: Da steh' ich nun, ich armer Tor"
]

def main():
    root = tk.Tk()
    root.title('Reimen mit Goethe')

    lbl = tk.Label(root, text='', wraplength=400, font=('Arial',14), justify='center')
    lbl.pack(padx=10, pady=10)

    def show():
        lbl.config(text=random.choice(GOETHE_LINES))

    tk.Button(root, text='Zeile anzeigen', command=show).pack()
    tk.Button(root, text='Beenden', command=root.destroy).pack(pady=6)
    root.mainloop()

if __name__ == '__main__':
    main()
