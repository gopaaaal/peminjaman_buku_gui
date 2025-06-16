import tkinter as tk

# List untuk menyimpan data
data_mahasiswa = []

# Fungsi-fungsi
def tambah():
    nama = entry_nama.get()
    nim = entry_nim.get()
    id_mhs = entry_id.get()
    if nama and nim and id_mhs:
        data = f"ID: {id_mhs} | Nama: {nama} | NIM: {nim}"
        data_mahasiswa.append(data)
        listbox.insert(tk.END, data)
        entry_id.delete(0, tk.END)
        entry_nama.delete(0, tk.END)
        entry_nim.delete(0, tk.END)
        label_output.config(text="Data berhasil ditambahkan.")
    else:
        label_output.config(text="Harap isi semua data!")

def update():
    selected_index = listbox.curselection()
    if selected_index:
        nama = entry_nama.get()
        nim = entry_nim.get()
        id_mhs = entry_id.get()
        if nama and nim and id_mhs:
            data = f"ID: {id_mhs} | Nama: {nama} | NIM: {nim}"
            data_mahasiswa[selected_index[0]] = data
            listbox.delete(selected_index)
            listbox.insert(selected_index, data)
            label_output.config(text="Data berhasil diupdate.")
        else:
            label_output.config(text="Harap isi semua data!")
    else:
        label_output.config(text="Pilih data yang akan diupdate!")

def hapus():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
        del data_mahasiswa[selected_index[0]]
        label_output.config(text="Data berhasil dihapus.")
    else:
        label_output.config(text="Pilih data yang akan dihapus!")
    
    # Kosongkan field input juga
    entry_id.delete(0, tk.END)
    entry_nama.delete(0, tk.END)
    entry_nim.delete(0, tk.END)

def isi_form(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_data = data_mahasiswa[selected_index[0]]
        parts = selected_data.split('|')
        id_mhs = parts[0].split(':')[1].strip()
        nama = parts[1].split(':')[1].strip()
        nim = parts[2].split(':')[1].strip()

        entry_id.delete(0, tk.END)
        entry_nama.delete(0, tk.END)
        entry_nim.delete(0, tk.END)
        entry_id.insert(0, id_mhs)
        entry_nama.insert(0, nama)
        entry_nim.insert(0, nim)

# Window Utama
root = tk.Tk()
root.title("Aplikasi CRUD Sederhana")

# Input ID
tk.Label(root, text="ID").grid(row=0, column=0, sticky="w")
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, columnspan=2, sticky="we")

# Input Nama
tk.Label(root, text="Nama").grid(row=1, column=0, sticky="w")
entry_nama = tk.Entry(root)
entry_nama.grid(row=1, column=1, columnspan=2, sticky="we")

# Input NIM
tk.Label(root, text="NIM").grid(row=2, column=0, sticky="w")
entry_nim = tk.Entry(root)
entry_nim.grid(row=2, column=1, columnspan=2, sticky="we")

# Tombol Tambah, Update, Hapus
tk.Button(root, text="Tambah", command=tambah, width=10).grid(row=3, column=0, padx=5, pady=10)
tk.Button(root, text="Update", command=update, width=10).grid(row=3, column=1, padx=5, pady=10)
tk.Button(root, text="Hapus", command=hapus, width=10).grid(row=3, column=2, padx=5, pady=10)

# Listbox untuk menampilkan semua data
listbox = tk.Listbox(root, width=50)
listbox.grid(row=4, column=0, columnspan=3, pady=10)
listbox.bind('<<ListboxSelect>>', isi_form)

# Output
label_output = tk.Label(root, text="", pady=10)
label_output.grid(row=5, column=0, columnspan=3)

root.mainloop() 