num = input("Enter a number: ")
power = len(num)
print("Armstrong" if sum(int(digit) ** power for digit in num) == int(num) else "Not Armstrong")
