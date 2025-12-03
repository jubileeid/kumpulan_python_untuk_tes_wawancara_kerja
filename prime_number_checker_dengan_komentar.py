# Program: Prime Number Checker
# Tujuan: Mengecek apakah sebuah angka merupakan bilangan prima
# Apa itu bilangan prima?
# - Bilangan prima adalah bilangan >1 yang hanya bisa dibagi 1 dan dirinya sendiri.
# - Contoh bilangan prima: 2, 3, 5, 7, 11, 13, ...
# - Contoh bukan bilangan prima: 4, 6, 8, 9, 10

# Meminta input dari pengguna
# int() digunakan untuk mengubah input string menjadi integer
angka = int(input("Masukkan angka untuk dicek: "))

# Bilangan prima harus lebih besar dari 1
if angka <= 1:
    print(angka, "bukan bilangan prima.")
else:
    # Asumsikan awalnya angka adalah prima
    is_prime = True

    # Loop dari 2 sampai sqrt(angka) untuk cek faktor
    # range(2, angka) juga bisa, tapi range(2, int(angka**0.5)+1) lebih efisien
    for i in range(2, int(angka ** 0.5) + 1):
        # Jika angka habis dibagi i → bukan prima
        if angka % i == 0:
            is_prime = False
            break  # tidak perlu cek angka lain

    # Menampilkan hasil
    if is_prime:
        print(angka, "adalah bilangan prima.")
    else:
        print(angka, "bukan bilangan prima.")
