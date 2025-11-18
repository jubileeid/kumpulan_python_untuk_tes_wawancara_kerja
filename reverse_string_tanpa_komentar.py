def reverse_string(text):
    return text[::-1]

user_input = input("Masukkan teks yang ingin dibalik: ")
result = reverse_string(user_input)
print("Hasil dibalik:", result)
