def numbers_divisible_by_9():
    return [n for n in range(100, 1000) if sum_of_digits(n) % 9 == 0]