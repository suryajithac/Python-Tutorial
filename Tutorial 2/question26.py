def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def separate_primes_composites(numbers):
    primes = []
    composites = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
        else:
            composites.append(num)
    return primes, composites