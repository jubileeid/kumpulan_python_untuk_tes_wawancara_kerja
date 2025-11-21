angka = [12, 5, 48, 7, 29, 3, 50, 17]

nilai_maksimum = max(angka)
nilai_minimum = min(angka)

print("Nilai maksimum:", nilai_maksimum)
print("Nilai minimum:", nilai_minimum)

maks_manual = angka[0]
min_manual = angka[0]

for nilai in angka:
    if nilai > maks_manual:
        maks_manual = nilai
    if nilai < min_manual:
        min_manual = nilai

print("Nilai maksimum (manual):", maks_manual)
print("Nilai minimum (manual):", min_manual)
