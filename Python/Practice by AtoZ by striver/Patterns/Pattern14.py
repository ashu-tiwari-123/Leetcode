n = 5
for i in range(n):
    for ch in range(ord('A'), ord('A') + i + 1):
        print(chr(ch), end=" ")
    print()
