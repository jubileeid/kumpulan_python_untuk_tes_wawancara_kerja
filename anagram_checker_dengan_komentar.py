# Program: Anagram Checker
# Tujuan program ini adalah memeriksa apakah dua kata merupakan "anagram".
# Apa itu anagram?
# ➤ Anagram adalah dua kata atau frasa yang memiliki huruf-huruf yang sama
#   dengan jumlah yang sama, tetapi susunannya berbeda.
#
# Contoh:
#   "listen" dan "silent" → anagram
#   "earth" dan "heart"   → anagram
#   "book" dan "cook"     → bukan anagram (huruf B dan C berbeda)
#
# Kita akan menggunakan dua cara:
# 1. Dengan menyortir huruf-hurufnya (sorted)
# 2. Dengan menghitung jumlah kemunculan setiap huruf (dictionary)


# ---------------------------------------------------------------------
# LANGKAH 1: Menerima input dari pengguna
# ---------------------------------------------------------------------

# Fungsi input() meminta pengguna mengetikkan sesuatu,
# lalu .lower() digunakan untuk mengubah semua huruf menjadi huruf kecil,
# agar perbandingan tidak sensitif terhadap huruf besar/kecil.
kata1 = input("Masukkan kata pertama: ").lower()
kata2 = input("Masukkan kata kedua: ").lower()


# ---------------------------------------------------------------------
# LANGKAH 2: Membersihkan spasi
# ---------------------------------------------------------------------

# Jika pengguna memasukkan frasa seperti "conversation" dan "voices rant on",
# maka kita perlu menghapus spasi agar bisa dibandingkan dengan benar.
kata1_bersih = kata1.replace(" ", "")
kata2_bersih = kata2.replace(" ", "")


# ---------------------------------------------------------------------
# CARA 1: Menggunakan sorted()
# ---------------------------------------------------------------------

# Fungsi sorted() mengurutkan huruf-huruf dalam string menjadi list.
# Contoh:
#   sorted("listen") → ['e','i','l','n','s','t']
#   sorted("silent") → ['e','i','l','n','s','t']
#
# Jika hasil sorted sama, berarti hurufnya sama dengan jumlah yang sama.
if sorted(kata1_bersih) == sorted(kata2_bersih):
    print("Kedua kata adalah anagram (menggunakan metode sorted).")
else:
    print("Kedua kata bukan anagram (menggunakan metode sorted).")


# ---------------------------------------------------------------------
# CARA 2: Menghitung jumlah huruf secara manual
# ---------------------------------------------------------------------

# Di sini kita membuat fungsi untuk menghitung berapa kali setiap huruf muncul.
# Caranya:
# - Buat dictionary kosong (misal: {'a':2, 'b':1, ...})
# - Loop semua huruf dalam teks
# - Jika huruf belum ada di dictionary, tambahkan dengan nilai 1
# - Jika huruf sudah ada, tambahkan nilainya 1 lagi
def hitung_karakter(teks):
    jumlah = {}  # dictionary untuk menyimpan jumlah huruf
    for huruf in teks:
        # .get(huruf, 0) artinya:
        # jika huruf sudah ada → ambil nilainya
        # jika belum ada      → gunakan nilai 0
        jumlah[huruf] = jumlah.get(huruf, 0) + 1
    return jumlah


# Bandingkan dictionary hasil penghitungan huruf
if hitung_karakter(kata1_bersih) == hitung_karakter(kata2_bersih):
    print("Kedua kata adalah anagram (menggunakan perhitungan huruf manual).")
else:
    print("Kedua kata bukan anagram (menggunakan perhitungan huruf manual).")
