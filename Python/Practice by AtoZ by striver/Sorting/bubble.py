arr = [9, 46, 52, 24, 20, 13]

def swap(n, j):
    temp = arr[n]
    arr[n] = arr[j]
    arr[j] = temp

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            swap(j,j+1)

print(arr)
