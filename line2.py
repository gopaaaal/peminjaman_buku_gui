from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_heigth=20
canvas_width=200
y = int(canvas_heigth / 2)
w.create_line(0 , y, canvas_width, y )
mainloop()