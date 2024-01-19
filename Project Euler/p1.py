toplam = 0

for sayi in range(1,10):
    if sayi % 3 == 0 or sayi % 5 == 0:
        toplam += sayi
    else:
        continue

print(toplam)