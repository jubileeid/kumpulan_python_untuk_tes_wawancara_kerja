# ============================================================
# Program: List Comprehension Examples
# Deskripsi:
#   Program ini menunjukkan berbagai contoh penggunaan
#   List Comprehension dalam Python.
#
# Apa itu List Comprehension?
#   List Comprehension adalah cara singkat untuk membuat list baru
#   berdasarkan iterable (seperti list, range, dsb.)
#
# Format umum:
#       [expression for item in iterable if condition]
#
# Manfaat:
#   - Kode lebih pendek
#   - Lebih mudah dibaca
#   - Lebih "Pythonic"
# ============================================================

# ------------------------------------------------------------
# 1. Membuat list angka 1 sampai 10
# ------------------------------------------------------------
numbers = [i for i in range(1, 11)]
print("1) List angka 1–10:", numbers)


# ------------------------------------------------------------
# 2. Membuat list kuadrat dari angka 1–10
#    Contoh dari: 1 → 1, 2 → 4, 3 → 9, dst.
# ------------------------------------------------------------
squares = [i * i for i in range(1, 11)]
print("2) Kuadrat dari 1–10:", squares)


# ------------------------------------------------------------
# 3. Mengambil hanya angka genap dari 1–20
#    Menggunakan kondisi if di dalam list comprehension
# ------------------------------------------------------------
evens = [i for i in range(1, 21) if i % 2 == 0]
print("3) Angka genap 1–20:", evens)


# ------------------------------------------------------------
# 4. Mengubah semua teks menjadi huruf besar
# ------------------------------------------------------------
words = ["python", "java", "excel", "canva"]
uppercase_words = [w.upper() for w in words]
print("4) UPPERCASE:", uppercase_words)


# ------------------------------------------------------------
# 5. Mengambil karakter vokal dari sebuah kata
# ------------------------------------------------------------
text = "programming"
vowels = [char for char in text if char in "aeiou"]
print("5) Vokal dalam 'programming':", vowels)


# ------------------------------------------------------------
# 6. Membuat list angka pangkat dua hanya untuk angka ganjil
# ------------------------------------------------------------
odd_squares = [i * i for i in range(1, 21) if i % 2 == 1]
print("6) Kuadrat angka ganjil 1–20:", odd_squares)


# ------------------------------------------------------------
# 7. List comprehension dengan kondisi dua tahap:
#    Ambil angka yang habis dibagi 3 dan > 10
# ------------------------------------------------------------
filtered = [i for i in range(1, 51) if i % 3 == 0 and i > 10]
print("7) Angka >10 dan habis dibagi 3:", filtered)


# ------------------------------------------------------------
# 8. Nested Loop dalam List Comprehension
#    Membuat pasangan (x, y) untuk x=1–3 dan y=1–3
# ------------------------------------------------------------
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print("8) Kombinasi pasangan (x, y):", pairs)


# ============================================================
# Ringkasan:
#   - List comprehension mempercepat pembuatan list
#   - Dapat menggunakan kondisi (if)
#   - Dapat melakukan operasi matematika
#   - Dapat menggunakan nested loop
#   - Lebih pendek, lebih efisien, lebih Pythonic
# ============================================================
