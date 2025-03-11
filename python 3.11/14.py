import math

def czy_pierwsza(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

print(czy_pierwsza(2))  # True
print(czy_pierwsza(3))  # True
print(czy_pierwsza(4))  # False
print(czy_pierwsza(17))  # True
print(czy_pierwsza(20))  # False
print(czy_pierwsza(1))  # False
