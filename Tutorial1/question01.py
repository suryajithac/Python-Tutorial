n = int(input("Enter number of values: "))
numbers = list(map(int, input("Enter numbers: ").split()))
print("Sum of even numbers:", sum(num for num in numbers if num % 2 == 0))
