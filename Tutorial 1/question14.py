def fibonacci():
    fib = [0, 1]
    for _ in range(8):
        fib.append(fib[-1] + fib[-2])
    return fib