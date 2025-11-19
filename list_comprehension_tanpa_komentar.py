numbers = [i for i in range(1, 11)]
print("1) List angka 1–10:", numbers)

squares = [i * i for i in range(1, 11)]
print("2) Kuadrat dari 1–10:", squares)

evens = [i for i in range(1, 21) if i % 2 == 0]
print("3) Angka genap 1–20:", evens)

words = ["python", "java", "excel", "canva"]
uppercase_words = [w.upper() for w in words]
print("4) UPPERCASE:", uppercase_words)

text = "programming"
vowels = [char for char in text if char in "aeiou"]
print("5) Vokal dalam 'programming':", vowels)

odd_squares = [i * i for i in range(1, 21) if i % 2 == 1]
print("6) Kuadrat angka ganjil 1–20:", odd_squares)

filtered = [i for i in range(1, 51) if i % 3 == 0 and i > 10]
print("7) Angka >10 dan habis dibagi 3:", filtered)

pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print("8) Kombinasi pasangan (x, y):", pairs)
