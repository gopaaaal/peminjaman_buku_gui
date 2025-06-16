import tkinter as tk
from tkinter import Tk, Entry, Button, StringVar

# Membuat window
window = Tk()
window.title("Kalkulator Sederhana")

# Membuat bidang input
input_text = StringVar()
input_field = Entry(window, textvariable=input_text, font=("Arial", 16), justify="right", bd=10, relief="ridge")
input_field.grid(row=0, column=0, columnspan=4)

# Fungsi untuk menangani klik tombol angka/operator
def button_click(button):
    current = input_text.get()
    input_text.set(current + button)

# Fungsi untuk menghitung hasil ekspresi
def calculate():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except:
        input_text.set("Error")

# Fungsi untuk menghapus input
def clear():
    input_text.set("")

# Daftar tombol dalam bentuk list of lists
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Menampilkan tombol pada GUI
row = 1
for button_row in buttons:
    col = 0
    for button in button_row:
        Button(window, text=button, width=5, font=("Arial", 14), height=2,
               command=lambda b=button: button_click(b) if b != '=' else calculate()
               ).grid(row=row, column=col, sticky="nsew")
        col += 1  # Pindah ke kolom berikutnya
    row += 1  # Pindah ke baris berikutnya

# Tombol untuk menghapus input
Button(window, text='C', width=5, font=("Arial", 14), height=2, command=clear).grid(row=row, column=0, sticky="nsew")

# Menjalankan loop utama Tkinter
window.mainloop()
