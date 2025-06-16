import tkinter
import tkinter
from tkinter import Tk, Entry, Button, StringVar

window = Tk()

window.title ( "kalkulator sederhana")

# Membuat bidang input
input_text = StringVar()
input_field = Entry(window, textvariable=input_text)
input_field.grid(row=0, column=0, columnspan=4)

def button_click(button_text):
    current = input_text.get()
    input_text.set(current + button_text)

def calculate():
    try:
        result = str(eval(input_text.get()))  
        input_text.set(result)
    except Exception as e:
        input_text.set("error")
        
def clear() :
    input_text.set("")
    
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
   
]
row = 1
col = 0

for button in buttons:
    Button(window, text=button, width=5, command=lambda button=button:
        button_click(button if button != '=' else calculate())).grid (row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1
        
        # Tombol untuk mengosongkan bidang input 
        Button(window, text='C', width=5, command=clear).grid(row=row, column=col)
        
        window.mainloop()