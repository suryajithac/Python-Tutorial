def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))