import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Membuat koneksi ke database
conn = sqlite3.connect('peminjaman_buku.db')
c = conn.cursor()

# Membuat tabel jika belum ada
c.execute('''
CREATE TABLE IF NOT EXISTS peminjaman (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_peminjam TEXT NOT NULL,
    judul_buku TEXT NOT NULL,
    tanggal_pinjam TEXT NOT NULL
)
''')
conn.commit()

def tambah_peminjaman():
    nama = entry_nama.get()
    judul = entry_judul.get()
    tanggal = entry_tanggal.get()

    if nama and judul and tanggal:
        c.execute('INSERT INTO peminjaman (nama_peminjam, judul_buku, tanggal_pinjam) VALUES (?, ?, ?)', (nama, judul, tanggal))
        conn.commit()
        messagebox.showinfo("Sukses", "Data peminjaman berhasil ditambahkan.")
        tampilkan_data()
        clear_entries()
    else:
        messagebox.showwarning("Peringatan", "Semua field harus diisi.")

def tampilkan_data():
    for item in tree.get_children():
        tree.delete(item)
    c.execute('SELECT * FROM peminjaman')
    rows = c.fetchall()
    for row in rows:
        tree.insert('', 'end', values=row)

def hapus_peminjaman():
    selected = tree.selection()
    if selected:
        item = tree.item(selected)
        id_peminjaman = item['values'][0]
        c.execute('DELETE FROM peminjaman WHERE id=?', (id_peminjaman,))
        conn.commit()
        messagebox.showinfo("Sukses", "Data peminjaman berhasil dihapus.")
        tampilkan_data()
    else:
        messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus.")

def clear_entries():
    entry_nama.delete(0, tk.END)
    entry_judul.delete(0, tk.END)
    entry_tanggal.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Aplikasi Peminjaman Buku")

frame_form = tk.Frame(root)
frame_form.pack(padx=10, pady=10)

tk.Label(frame_form, text="Nama Peminjam:").grid(row=0, column=0, sticky='w')
entry_nama = tk.Entry(frame_form, width=30)
entry_nama.grid(row=0, column=1, pady=5)

tk.Label(frame_form, text="Judul Buku:").grid(row=1, column=0, sticky='w')
entry_judul = tk.Entry(frame_form, width=30)
entry_judul.grid(row=1, column=1, pady=5)

tk.Label(frame_form, text="Tanggal Pinjam (YYYY-MM-DD):").grid(row=2, column=0, sticky='w')
entry_tanggal = tk.Entry(frame_form, width=30)
entry_tanggal.grid(row=2, column=1, pady=5)

btn_tambah = tk.Button(root, text="Tambah Peminjaman", command=tambah_peminjaman)
btn_tambah.pack(pady=5)

btn_hapus = tk.Button(root, text="Hapus Peminjaman", command=hapus_peminjaman)
btn_hapus.pack(pady=5)

columns = ('ID', 'Nama Peminjam', 'Judul Buku', 'Tanggal Pinjam')
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
tree.pack(padx=10, pady=10, fill='both', expand=True)

tampilkan_data()

root.mainloop()

conn.close()
