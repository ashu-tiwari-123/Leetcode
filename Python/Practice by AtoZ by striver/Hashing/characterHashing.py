size = int(input("Enter the number of elements in the array: "))
arr = []

for i in range(size):
    num = input("Enter a lowercase character (a-z): ")
    arr.append(num)

# Create a hash array of size 26 for letters a-z
hash_arr = [0] * 26

# Count frequency
for i in range(size):
    index = ord(arr[i]) - ord('a')
    if 0 <= index < 26:
        hash_arr[index] += 1

# Query
q = int(input("Enter number of queries: "))
for i in range(q):
    val = input("Enter character to find its count: ")
    index = ord(val) - ord('a')
    if 0 <= index < 26:
        print(f"Count of '{val}' is {hash_arr[index]}")
    else:
        print("Character out of range (a-z)")
