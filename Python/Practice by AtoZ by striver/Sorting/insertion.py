arr = [14,9,15,12,8,6,13]

for i in range(len(arr)):
    j = i
    while(j>0 and arr[j-1]>arr[j]):
        arr[j] , arr[j-1] = arr[j-1] , arr[j]
        j-=1

print(arr)            