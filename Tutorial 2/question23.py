def find_mode(numbers):
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1
    return max(count_dict, key=count_dict.get)