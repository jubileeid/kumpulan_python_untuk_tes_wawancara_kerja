nama_file = "contoh.txt"

with open(nama_file, "w") as file:
    file.write("Ini adalah contoh penulisan file.\n")
    file.write("Belajar Python itu menyenangkan!\n")
    file.write("File I/O adalah konsep dasar yang sering digunakan.\n")

with open(nama_file, "r") as file:
    isi_file = file.read()

print("=== Isi File ===")
print(isi_file)
