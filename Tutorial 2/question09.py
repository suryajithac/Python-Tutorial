def reverse_halves(s):
    mid = len(s) // 2
    first_half = s[:mid][::-1]
    second_half = s[mid:][::-1]
    return first_half + second_half