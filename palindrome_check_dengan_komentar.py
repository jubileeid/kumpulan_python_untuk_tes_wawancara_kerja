# ============================================================
# Program: Palindrome Check
# Deskripsi:
#   Program ini mengecek apakah suatu kata atau kalimat
#   merupakan PALINDROME.
#
# Apa itu Palindrome?
#   Palindrome adalah kata/kalimat yang jika dibaca dari depan
#   maupun belakang menghasilkan teks yang sama.
#
# Contoh:
#   "level"  → palindrome (sama dibaca dari depan & belakang)
#   "madam"  → palindrome
#   "python" → bukan palindrome
#
# Catatan:
#   String akan dinormalisasi terlebih dahulu (huruf kecil semua)
#   dan semua spasi atau simbol bisa dihapus (opsional).
# ============================================================


def is_palindrome(text):
    """
    Fungsi untuk mengecek apakah string 'text' merupakan palindrome.

    Tahapan:
        1. Normalisasi string (lowercase)
        2. Menghapus spasi (jika ingin cek kata/kalimat)
        3. Membalik string menggunakan slicing
        4. Membandingkan versi asli dengan versi terbalik

    Return:
        True  → jika palindrome
        False → jika bukan palindrome
    """

    # ------------------------------------------------------------
    # 1. Mengubah huruf menjadi lowercase agar perbandingan konsisten.
    #    Misalnya "Level" dan "level" dianggap sama.
    # ------------------------------------------------------------
    normalized = text.lower()

    # ------------------------------------------------------------
    # 2. Menghapus spasi di dalam kalimat jika diperlukan.
    #    Contoh: "A nut for a jar of tuna" → palindrome
    #
    # Jika ingin mempertahankan spasi, baris ini bisa dihapus.
    # ------------------------------------------------------------
    normalized = normalized.replace(" ", "")

    # ------------------------------------------------------------
    # 3. Membalik string dengan slicing.
    #    normalized[::-1] berarti mengambil semua karakter,
    #    tapi dengan langkah -1 (mundur).
    # ------------------------------------------------------------
    reversed_text = normalized[::-1]

    # ------------------------------------------------------------
    # 4. Membandingkan string asli (yang sudah dinormalisasi)
    #    dengan versi terbaliknya.
    # ------------------------------------------------------------
    return normalized == reversed_text


# ============================================================
# Bagian utama program
# ============================================================

# Meminta input dari pengguna
user_input = input("Masukkan kata atau kalimat untuk dicek palindrome: ")

# Mengecek apakah input palindrome
if is_palindrome(user_input):
    print("Hasil: Ini adalah PALINDROME.")
else:
    print("Hasil: Ini BUKAN palindrome.")

# ============================================================
# Ringkasan:
#   - Palindrome berarti sama dibaca dari depan dan belakang
#   - strtolower() dan replace() membantu normalisasi
#   - Slicing text[::-1] adalah cara paling sederhana membalik string
# ============================================================
