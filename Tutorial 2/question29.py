def remove_duplicate_elements(lst):
    unique_items = []
    for item in lst:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items