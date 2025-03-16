def multiplication_table(n):
    for i in range(1, n+1):
        print(*[i*j for j in range(1, 11)])