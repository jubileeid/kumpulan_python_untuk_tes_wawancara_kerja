# ============================================================
# Program: Fibonacci Sequence
# Deskripsi:
#   Program ini menghasilkan deret Fibonacci hingga jumlah elemen
#   tertentu (misalnya 10 angka pertama).
#
# Apa itu Deret Fibonacci?
#   Deret angka di mana setiap angka merupakan hasil penjumlahan
#   dua angka sebelumnya.
#
#   Rumus:
#       F0 = 0
#       F1 = 1
#       Fn = F(n-1) + F(n-2)
#
# Contoh:
#   0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#
# Tujuan Pembelajaran:
#   - Memahami cara kerja loop
#   - Mengerti konsep penjumlahan berurutan
#   - Memahami bagaimana variabel berubah di dalam loop
# ============================================================


def fibonacci(n):
    """
    Fungsi untuk menghasilkan deret Fibonacci sebanyak n angka.
    Return berupa list berisi urutan angka Fibonacci.

    Parameter:
        n (int): jumlah elemen deret Fibonacci yang ingin ditampilkan

    Contoh:
        fibonacci(5) → [0, 1, 1, 2, 3]
    """

    # Jika n <= 0 maka kembalikan list kosong
    if n <= 0:
        return []

    # Jika n == 1 maka hanya tampilkan angka pertama yaitu 0
    if n == 1:
        return [0]

    # ------------------------------------------------------------
    # Inisialisasi dua angka pertama Fibonacci
    # a = 0 (F0)
    # b = 1 (F1)
    #
    # Lalu kita simpan keduanya ke dalam list hasil
    # ------------------------------------------------------------
    result = [0, 1]
    a, b = 0, 1

    # ------------------------------------------------------------
    # Loop dimulai dari elemen ke-3 hingga ke-n
    # Setiap iterasi:
    #   angka baru = a + b
    #   lalu pergeseran nilai:
    #       a ← b
    #       b ← angka baru
    # ------------------------------------------------------------
    for _ in range(2, n):
        next_number = a + b
        result.append(next_number)

        # Perbarui dua angka terakhir untuk iterasi selanjutnya
        a, b = b, next_number

    return result


# ============================================================
# Bagian utama program
# ============================================================

# Meminta jumlah elemen Fibonacci dari pengguna
n = int(input("Masukkan jumlah angka Fibonacci yang ingin ditampilkan: "))

# Menghasilkan deret Fibonacci
fib_sequence = fibonacci(n)

# Menampilkan hasil
print("Deret Fibonacci:", fib_sequence)

# ============================================================
# Ringkasan:
#   - Fibonacci adalah deret yang setiap angkanya adalah jumlah
#     dua angka sebelumnya
#   - Inisialisasi awal selalu 0 dan 1
#   - Gunakan loop untuk menghasilkan angka selanjutnya
# ============================================================
