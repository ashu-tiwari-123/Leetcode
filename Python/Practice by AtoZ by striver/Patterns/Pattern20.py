n = 5
space = 2 * n - 2  # total middle space initially

for i in range(2 * n - 1):
    if i < n:
        stars = i + 1
    else:
        stars = 2 * n - i - 1

    for j in range(stars):
        print("x", end=" ")

    for s in range(space):
        print(" ", end=" ")

    for j in range(stars):
        print("x", end=" ")

    print()

    if i < n - 1:
        space -= 2
    else:
        space += 2
