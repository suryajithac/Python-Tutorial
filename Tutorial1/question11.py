seconds = int(input("Enter time in seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")
