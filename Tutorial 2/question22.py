def find_median(numbers):
    numbers.sort()
    middle = len(numbers) // 2
    return numbers[middle]