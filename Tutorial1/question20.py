low, high = map(int, input("Enter lower and upper limit: ").split())
print("Sum of odd numbers:", sum(i for i in range(low, high+1) if i % 2 != 0))
