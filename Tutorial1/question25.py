a, b, c = sorted(map(int, input("Enter three sides: ").split()))
print("Right-angled triangle" if a**2 + b**2 == c**2 else "Not a right-angled triangle")
