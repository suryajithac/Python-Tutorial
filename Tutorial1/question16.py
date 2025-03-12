print([num for num in range(100, 1001) if sum(map(int, str(num))) % 9 == 0])
