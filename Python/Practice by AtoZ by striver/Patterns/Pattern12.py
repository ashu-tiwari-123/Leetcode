n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")

    spaces = (n - i) * 2
    for s in range(spaces):
        print(" ", end="")

    for num in range(i, 0, -1):
        print(num, end="")

    print()
