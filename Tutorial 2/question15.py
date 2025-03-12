def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def check_sign(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result