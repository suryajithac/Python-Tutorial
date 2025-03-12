def completely_remove_duplicates(lst):
    return [x for x in lst if lst.count(x) == 1]