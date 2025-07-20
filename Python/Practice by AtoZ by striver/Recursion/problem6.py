arr = []
n = int(input("Enter the size of list: "))
for i in range(n):
    value = int(input(f"Enter the {i} element: "))
    arr.append(value)

print(f"Previous Array: {arr}")

def swap_elements(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    return lst

# Two Pointer Method
# def reverseArray(i, n, arr):
#     if i >= n:
#         return
#     swap_elements(arr, i, n)
#     reverseArray(i + 1, n - 1, arr)

# Single pointer method
def reverseArray(i,n,arr):
    if(i>=n//2):return
    swap_elements(arr,i,n-i-1)
    reverseArray(i+1,n,arr)

reverseArray(0, n, arr)
print(f"Reversed Array: {arr}")
