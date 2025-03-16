import math
def quadratic_roots(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        return root1, root2
    else:
        return "No real roots"