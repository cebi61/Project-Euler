a,b = 1,2
toplam = 0

while a <= 4000000:
    if a % 2 == 0:
        toplam += a
    a, b = b, a + b

print(toplam)