def sum_of_cubes_even(n):
    return sum(x**3 for x in range(2, n+1, 2))