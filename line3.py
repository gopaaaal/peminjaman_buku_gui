
from tkinter import *
master = Tk()
master.title ('kelamin')
var1 = IntVar()
Checkbutton (master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton (master, text='female', variable=var2).grid(row=2, sticky=W)
mainloop()