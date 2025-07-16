n = int(input("Enter the number: "))

is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):  # Efficient check up to sqrt(n)
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")
