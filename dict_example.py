# dict_example.py

# Membuat dictionary
mahasiswa = {
    "nama": "Budi",
    "nim": "2023001",
    "jurusan": "Informatika"
}

# Menampilkan dictionary
print("Data mahasiswa:", mahasiswa)

# Mengakses nilai
print("Nama:", mahasiswa["nama"])

# Menambah data
mahasiswa["semester"] = 2
print("Setelah ditambah:", mahasiswa)

# Mengubah data
mahasiswa["nama"] = "Andi"
print("Setelah diubah:", mahasiswa)
