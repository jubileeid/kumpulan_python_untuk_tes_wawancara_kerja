angka = int(input("Masukkan angka untuk dicek: "))

if angka <= 1:
    print(angka, "bukan bilangan prima.")
else:
    is_prime = True
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            is_prime = False
            break
    if is_prime:
        print(angka, "adalah bilangan prima.")
    else:
        print(angka, "bukan bilangan prima.")
