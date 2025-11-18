# ============================================================
# Program: Reverse String
# Deskripsi:
#   Program ini akan membalik urutan karakter dari sebuah string.
#   Misalnya: "Python" → "nohtyP"
#
# Tujuan Pembelajaran:
#   - Memahami bagaimana string bekerja di Python.
#   - Mengenal teknik slicing (fitur Python yang sangat powerful).
#   - Mengerti bahwa string di Python bersifat immutable.
#   - Melihat cara membuat fungsi sederhana yang rapi dan reusable.
#
# Catatan:
#   Kode ini ditulis dengan komentar yang lengkap seperti tutorial,
#   sehingga cocok untuk pemula yang ingin memahami konsep dari nol.
# ============================================================


def reverse_string(text):
    """
    Fungsi reverse_string() menerima sebuah string lalu mengembalikan
    versi terbalik dari string tersebut.

    Parameter:
        text (str) → string yang ingin dibalik

    Return:
        str → string hasil pembalikan

    Contoh:
        reverse_string("Python") → "nohtyP"
    """

    # ------------------------------------------------------------
    # Di Python, string bersifat IMMUTABLE.
    # Artinya: kita tidak bisa mengubah karakter di dalamnya secara langsung.
    # Jadi untuk membalik string, kita membuat string baru dengan cara tertentu.
    # ------------------------------------------------------------

    # ------------------------------------------------------------
    # Cara paling Pythonic untuk membalik string adalah menggunakan SLICING.
    #
    # Format umum slicing:
    #   text[start:end:step]
    #
    # Jika step = -1 → maka kita bergerak dari belakang ke depan (terbalik)
    # ------------------------------------------------------------
    reversed_text = text[::-1]

    # Keterangan text[::-1]:
    #   - start  : kosong → artinya mulai dari akhir string
    #   - end    : kosong → terus sampai ke awal string
    #   - step   : -1    → bergerak mundur satu per satu
    #
    # Contoh jika text = "Python"
    #   Index:  P  y  t  h  o  n
    #   Posisi: 0  1  2  3  4  5
    #
    # text[::-1] akan mengambil:
    #   mulai dari index terakhir → n
    #   lalu ke 4 → o
    #   lalu ke 3 → h
    #   lalu ke 2 → t
    #   lalu ke 1 → y
    #   lalu ke 0 → P
    #
    # sehingga hasilnya: "nohtyP"

    return reversed_text


# ============================================================
# Bagian utama program (main program)
# Di bawah ini kita meminta input dari pengguna dan menampilkan hasilnya.
# ============================================================

# Meminta input dari pengguna
user_input = input("Masukkan teks yang ingin dibalik: ")

# Memanggil fungsi reverse_string untuk membalik string
result = reverse_string(user_input)

# Menampilkan hasil pembalikan
print("Hasil dibalik:", result)

# Selesai.
# ============================================================
# Ringkasan:
#   - String adalah immutable → tidak bisa diubah langsung
#   - Slicing adalah teknik powerful: text[::-1]
#   - Fungsi dibuat agar bisa dipakai ulang dengan mudah
# ============================================================
