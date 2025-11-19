# ============================================================
# Program: Count Characters & Count Words
# Deskripsi:
#   Program ini menghitung:
#       1. Jumlah karakter (Character Count)
#       2. Jumlah kata (Word Count)
#
# Catatan:
#   - Character Count menghitung semua karakter kecuali spasi.
#   - Word Count menghitung kata berdasarkan pemisah spasi.
#
# Tujuan Pembelajaran:
#   - Memahami manipulasi string
#   - Menggunakan fungsi len()
#   - Memahami perbedaan karakter dan kata
#   - Menggunakan split() untuk memecah kalimat
# ============================================================


def count_characters(text):
    """
    Menghitung jumlah karakter (tanpa spasi).

    Contoh:
        text = "Hello World"
        → karakter = 10 (spasi tidak dihitung)
    """

    # Menghapus semua spasi sebelum dihitung
    text_no_spaces = text.replace(" ", "")

    # Menghitung jumlah karakter
    return len(text_no_spaces)


def count_words(text):
    """
    Menghitung jumlah kata dalam kalimat.
    split() akan memecah text berdasarkan spasi.

    Contoh:
        "saya belajar python"
        → 3 kata
    """

    # Memecah kalimat menjadi list kata-kata
    words = text.split()

    # Panjang list = jumlah kata
    return len(words)


# ============================================================
# Bagian utama program
# ============================================================

# Meminta input dari pengguna
user_input = input("Masukkan kalimat: ")

# Menghitung jumlah karakter (tanpa spasi)
char_count = count_characters(user_input)

# Menghitung jumlah kata
word_count = count_words(user_input)

# Menampilkan hasil
print("Jumlah karakter (tanpa spasi):", char_count)
print("Jumlah kata:", word_count)

# ============================================================
# Ringkasan:
#   - replace(" ", "") menghapus spasi untuk character count
#   - split() memecah kalimat menjadi list kata
#   - len() menghitung panjang string atau list
# ============================================================
