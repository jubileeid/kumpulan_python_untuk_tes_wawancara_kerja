# Program: Simple File I/O (Input/Output)
# Tujuan:
# 1. Menulis teks ke dalam sebuah file
# 2. Membaca isi file kembali dan menampilkannya ke layar

# --- MENULIS KE FILE ---

# Nama file yang ingin digunakan.
# Jika file tidak ada, Python akan membuatnya secara otomatis.
nama_file = "contoh.txt"

# Membuka file dalam mode "w" (write).
# Mode "w" akan membuat file baru atau menimpa isi file jika sudah ada.
with open(nama_file, "w") as file:
    # Menulis beberapa baris teks ke dalam file
    file.write("Ini adalah contoh penulisan file.\n")
    file.write("Belajar Python itu menyenangkan!\n")
    file.write("File I/O adalah konsep dasar yang sering digunakan.\n")

# Setelah keluar dari blok "with", file otomatis tertutup.


# --- MEMBACA DARI FILE ---

# Membuka file dalam mode "r" (read)
# Mode "r" digunakan untuk membaca isi file yang sudah ada.
with open(nama_file, "r") as file:
    # Menggunakan read() untuk mengambil seluruh isi file sebagai satu string
    isi_file = file.read()

# Menampilkan isi file ke layar
print("=== Isi File ===")
print(isi_file)
