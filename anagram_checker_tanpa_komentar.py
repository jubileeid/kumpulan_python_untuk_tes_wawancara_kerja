kata1 = input("Masukkan kata pertama: ").lower()
kata2 = input("Masukkan kata kedua: ").lower()

kata1_bersih = kata1.replace(" ", "")
kata2_bersih = kata2.replace(" ", "")

if sorted(kata1_bersih) == sorted(kata2_bersih):
    print("Kedua kata adalah anagram (dengan sorted).")
else:
    print("Kedua kata bukan anagram (dengan sorted).")

def hitung_karakter(teks):
    jumlah = {}
    for huruf in teks:
        jumlah[huruf] = jumlah.get(huruf, 0) + 1
    return jumlah

if hitung_karakter(kata1_bersih) == hitung_karakter(kata2_bersih):
    print("Kedua kata adalah anagram (dengan perhitungan karakter).")
else:
    print("Kedua kata bukan anagram (dengan perhitungan karakter).")
