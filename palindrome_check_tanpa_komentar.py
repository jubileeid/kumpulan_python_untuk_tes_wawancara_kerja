def is_palindrome(text):
    normalized = text.lower().replace(" ", "")
    return normalized == normalized[::-1]

user_input = input("Masukkan kata atau kalimat untuk dicek palindrome: ")
if is_palindrome(user_input):
    print("Hasil: Ini adalah PALINDROME.")
else:
    print("Hasil: Ini BUKAN palindrome.")
