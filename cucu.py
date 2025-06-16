import tkinter
from tkinter import Tk, Entry, Button, StringVar

window = Tk()
window.title("Kalkulator Sederhana")

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
    except Exception:
        input_text.set("error")

def clear():
    input_text.set("")

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

row = 1

for button_row in buttons:  # Loop untuk setiap baris
    col = 0
    for button in button_row:  # Loop untuk setiap tombol dalam baris
        Button(window, text=button, width=5, 
               command=lambda b=button: button_click(b) if b != '=' else calculate()
               ).grid(row=row, column=col)
        col += 1
    row += 1

# Tombol untuk menghapus input
Button(window, text='C', width=5, command=clear).grid(row=row, column=0)

# Menjalankan aplikasi
window.mainloop()
