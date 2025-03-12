def separate_types(lst):
    integers = []
    floats = []
    strings = []
    for item in lst:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, float):
            floats.append(item)
        else:
            strings.append(item)
    return integers, floats, strings