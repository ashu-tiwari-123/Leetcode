n= 5
for i in range(n):
    for ch in range(ord('A'),ord('A')+n-i):
        print(chr(ch), end=" ")
    print(' ')    