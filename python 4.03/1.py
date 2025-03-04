from sympy import *


def prime_selector(numbers: list[int]):
    prime_numbers = []
    for number in numbers:
        if isprime(number):
            prime_numbers.append(number)
    return prime_numbers


print(prime_selector(numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]))
