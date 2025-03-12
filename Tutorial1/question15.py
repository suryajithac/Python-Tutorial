num = int(input("Enter a number: "))
factor = 2
while num > 1:
    while num % factor == 0:
        print(factor, end=" ")
        num //= factor
    factor += 1
