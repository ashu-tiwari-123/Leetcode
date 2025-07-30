arr = [9, 46, 52, 24, 20, 13]

def swap(n, j):
    temp = arr[n]
    arr[n] = arr[j]
    arr[j] = temp

for i in range(len(arr)):
    mini = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[mini]:
            mini = j
    swap(i, mini)

print(arr)
