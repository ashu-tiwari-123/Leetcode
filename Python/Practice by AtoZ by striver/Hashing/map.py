from collections import Counter
n = int(input("Enter size of array"))
arr =[]
for i in range(n):
    v=int(input("Enter the value for array:"))
    arr.append(v)

mpp = Counter(arr)
q = int(input("Enter number of queries: "))
for i in range(q):
    val = int(input("Enter number to find its count: "))
    print(mpp[val])
    
