def is_armstrong(n):
    digits = list(map(int, str(n)))
    return n == sum(d**len(digits) for d in digits)