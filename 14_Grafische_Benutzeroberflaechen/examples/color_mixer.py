import tkinter as tk

def rgb_to_hex(r,g,b):
    return '#%02x%02x%02x' % (int(r),int(g),int(b))

def main():
    root = tk.Tk()
    root.title('Farbmischer')

    canvas = tk.Canvas(root, width=200, height=100)
    canvas.pack(pady=8)

    vars = [tk.IntVar(value=128) for _ in range(3)]

    def update(*_):
        h = rgb_to_hex(vars[0].get(), vars[1].get(), vars[2].get())
        canvas.delete('all')
        canvas.create_rectangle(0,0,200,100, fill=h, width=0)

    for i, name in enumerate(('R','G','B')):
        tk.Scale(root, from_=0, to=255, orient='horizontal', label=name, variable=vars[i], command=update).pack(fill='x')

    update()
    root.mainloop()

if __name__ == '__main__':
    main()
