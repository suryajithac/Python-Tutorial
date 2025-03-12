def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sin_series(x, n):
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result