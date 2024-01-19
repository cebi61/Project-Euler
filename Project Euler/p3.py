import math 

def prime_check(x):
    is_prime = True

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            is_prime = False
            continue
    return is_prime

sayi = 600851475143
biggest_prime = 1

for i in range(2, int(math.sqrt(sayi)) + 1):
    if sayi % i == 0 and prime_check(i):
        biggest_prime = i

print(biggest_prime)
