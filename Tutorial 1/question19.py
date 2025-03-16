def count_even_odd(numbers):
    evens = sum(1 for n in numbers if n % 2 == 0)
    odds = len(numbers) - evens
    return evens, odds