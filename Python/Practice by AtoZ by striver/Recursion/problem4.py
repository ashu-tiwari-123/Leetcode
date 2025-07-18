n = int(input("Enter the number: "))

def number(i, n):
    if i > n:
        return 0
    return i + number(i + 1, n)

res = number(1, n)
print("Sum from 1 to", n, "is:", res)
