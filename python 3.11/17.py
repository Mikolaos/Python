def factorial(n):
    if n < 0:
        raise ValueError("n nie może być liczbą ujemną")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(5))  # 120
