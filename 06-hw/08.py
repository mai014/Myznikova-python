n = 10
while n <= 99:
    a = n // 10
    b = n % 10
    if a * b * 3 == n:
        print(n)
    n += 1