# Program untuk menemukan nilai maksimum dan minimum dalam sebuah list

# Daftar angka sebagai contoh
angka = [12, 5, 48, 7, 29, 3, 50, 17]

# Menampilkan daftar angka
print("Daftar angka:", angka)

# Menggunakan fungsi built-in max() untuk mendapatkan nilai terbesar
nilai_maksimum = max(angka)

# Menggunakan fungsi built-in min() untuk mendapatkan nilai terkecil
nilai_minimum = min(angka)

# Menampilkan hasil
print("Nilai maksimum:", nilai_maksimum)
print("Nilai minimum:", nilai_minimum)

# ---------------------------------------------------------------------

# Alternatif: Menemukan max dan min secara manual (tanpa fungsi built-in)

# Menginisialisasi nilai awal
maks_manual = angka[0]   # Asumsikan elemen pertama sebagai nilai maksimum
min_manual = angka[0]    # Asumsikan elemen pertama sebagai nilai minimum

# Melakukan iterasi pada setiap angka dalam list
for nilai in angka:
    # Jika nilai lebih besar dari maks_manual, update maks_manual
    if nilai > maks_manual:
        maks_manual = nilai
    
    # Jika nilai lebih kecil dari min_manual, update min_manual
    if nilai < min_manual:
        min_manual = nilai

# Menampilkan hasil manual
print("Nilai maksimum (manual):", maks_manual)
print("Nilai minimum (manual):", min_manual)
