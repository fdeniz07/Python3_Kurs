import random
import tkinter as tk

CELL = 20
ROWS = 16
COLS = 24

def random_color():
    return "#%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def draw_grid(canvas):
    canvas.delete('all')
    for r in range(ROWS):
        for c in range(COLS):
            x0 = c*CELL
            y0 = r*CELL
            x1 = x0 + CELL
            y1 = y0 + CELL
            canvas.create_rectangle(x0,y0,x1,y1,fill=random_color(),width=0)

def main():
    root = tk.Tk()
    root.title('Grid Coloring — Farbfelder')
    canvas = tk.Canvas(root, width=COLS*CELL, height=ROWS*CELL)
    canvas.pack()

    frame = tk.Frame(root)
    frame.pack(fill='x')
    tk.Button(frame, text='Neu', command=lambda: draw_grid(canvas)).pack(side='left')
    tk.Button(frame, text='Speichern (PNG nicht implementiert)', command=lambda: None).pack(side='left')

    draw_grid(canvas)
    root.mainloop()

if __name__ == '__main__':
    main()
