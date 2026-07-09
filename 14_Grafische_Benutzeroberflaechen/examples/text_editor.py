import tkinter as tk
from tkinter import filedialog, messagebox

def main():
    root = tk.Tk()
    root.title('Einfacher Texteditor')

    text = tk.Text(root, wrap='word')
    text.pack(expand=True, fill='both')

    def open_file():
        path = filedialog.askopenfilename(filetypes=[('Text','*.txt'),('All files','*.*')])
        if path:
            with open(path, 'r', encoding='utf8') as f:
                text.delete('1.0','end')
                text.insert('1.0', f.read())

    def save_file():
        path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text','*.txt')])
        if path:
            with open(path, 'w', encoding='utf8') as f:
                f.write(text.get('1.0','end'))
                messagebox.showinfo('Gespeichert', f'Datei gespeichert: {path}')

    men = tk.Menu(root)
    filem = tk.Menu(men, tearoff=False)
    filem.add_command(label='Öffnen', command=open_file)
    filem.add_command(label='Speichern', command=save_file)
    filem.add_separator()
    filem.add_command(label='Beenden', command=root.destroy)
    men.add_cascade(label='Datei', menu=filem)
    root.config(menu=men)

    root.mainloop()

if __name__ == '__main__':
    main()
