# ============================================================
# Program: FizzBuzz
# Deskripsi:
#   FizzBuzz adalah salah satu soal paling terkenal untuk tes
#   programmer junior hingga menengah.
#
# Aturan:
#   - Jika sebuah angka habis dibagi 3, cetak "Fizz"
#   - Jika habis dibagi 5, cetak "Buzz"
#   - Jika habis dibagi 3 dan 5, cetak "FizzBuzz"
#   - Jika tidak memenuhi kondisi apa pun, cetak angkanya sendiri
#
# Contoh:
#   1 → 1
#   3 → Fizz
#   5 → Buzz
#   15 → FizzBuzz
#
# Tujuan Pembelajaran:
#   - Memahami penggunaan loop (for)
#   - Memahami operator modulus (%)
#   - Melatih pengambilan keputusan (if-elif-else)
#   - Membuat logika yang urut dan rapih
# ============================================================


def fizzbuzz(n):
    """
    Fungsi untuk mencetak FizzBuzz dari angka 1 sampai n.

    Parameter:
        n (int) → batas akhir deretan angka

    Fungsi ini tidak mengembalikan nilai,
    tetapi langsung mencetak hasil FizzBuzz ke layar.
    """

    # Melakukan perulangan dari angka 1 sampai n
    for i in range(1, n + 1):

        # --------------------------------------------------------
        # Mengecek kondisi paling spesifik terlebih dahulu:
        #   i % 3 == 0 dan i % 5 == 0
        #
        # Mengapa kondisi ini harus dicek dulu?
        #   Karena jika hanya mengecek i % 3 == 0 atau i % 5 == 0 dulu,
        #   maka angka seperti 15 akan ketangkap oleh salah satu kondisi,
        #   sehingga tidak pernah mencapai kondisi "FizzBuzz".
        # --------------------------------------------------------
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        # Jika hanya habis dibagi 3 → Fizz
        elif i % 3 == 0:
            print("Fizz")

        # Jika hanya habis dibagi 5 → Buzz
        elif i % 5 == 0:
            print("Buzz")

        # Jika tidak habis dibagi 3 atau 5 → cetak angkanya
        else:
            print(i)


# ============================================================
# Bagian utama program
# ============================================================

# Meminta batas angka dari pengguna
n = int(input("Masukkan angka batas untuk FizzBuzz: "))

# Memanggil fungsi fizzbuzz
fizzbuzz(n)

# ============================================================
# Ringkasan:
#   - Urutan pengecekan IF sangat penting
#   - Modulus (%) menguji apakah angka habis dibagi bilangan tertentu
#   - Loop berjalan dari 1 sampai n
# ============================================================
