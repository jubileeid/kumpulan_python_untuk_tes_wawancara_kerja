def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    result = [0, 1]
    a, b = 0, 1

    for _ in range(2, n):
        next_number = a + b
        result.append(next_number)
        a, b = b, next_number

    return result

n = int(input("Masukkan jumlah angka Fibonacci yang ingin ditampilkan: "))
print("Deret Fibonacci:", fibonacci(n))
