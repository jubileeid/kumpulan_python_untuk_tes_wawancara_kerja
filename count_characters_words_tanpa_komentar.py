def count_characters(text):
    return len(text.replace(" ", ""))

def count_words(text):
    return len(text.split())

user_input = input("Masukkan kalimat: ")

char_count = count_characters(user_input)
word_count = count_words(user_input)

print("Jumlah karakter (tanpa spasi):", char_count)
print("Jumlah kata:", word_count)
