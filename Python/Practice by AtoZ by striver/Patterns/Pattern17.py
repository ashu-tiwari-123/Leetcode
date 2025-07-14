n = 4
for i in range(n):
    c = ord('A')
    b = (2 * i + 1) // 2
    for s in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print(chr(c), end=" ")
        if j < b:
            c += 1
        else:
            c -= 1
    print()
