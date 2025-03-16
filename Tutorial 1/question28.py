def sum_of_odds(lower, upper):
    return sum(n for n in range(lower, upper + 1) if n % 2 != 0)