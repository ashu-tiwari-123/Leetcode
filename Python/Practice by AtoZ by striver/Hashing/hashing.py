size = int(input("Enter the number of elements in the array: "))
arr = []

for i in range(size):
    num = int(input("Enter the number for array: "))
    arr.append(num)

# Create a hash array of size 13 (index 0 to 12)
hash_arr = [0] * 13

# Count frequency
for i in range(size):
    if arr[i] >= 0 and arr[i] < 13:
        hash_arr[arr[i]] += 1

# Query
q = int(input("Enter number of queries: "))
for i in range(q):
    val = int(input("Enter number to find its count: "))
    if val >= 0 and val < 13:
        print(f"Count of {val} is {hash_arr[val]}")
    else:
        print("Number out of range (0-12)")
