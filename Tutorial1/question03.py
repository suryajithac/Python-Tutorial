nums = list(map(int, input("Enter 4 numbers: ").split()))
pos = [num for num in nums if num > 0]
neg = [num for num in nums if num < 0]
print(f"Sum of positives: {sum(pos)}, Average: {sum(pos)/len(pos) if pos else 0}")
print(f"Sum of negatives: {sum(neg)}, Average: {sum(neg)/len(neg) if neg else 0}")
