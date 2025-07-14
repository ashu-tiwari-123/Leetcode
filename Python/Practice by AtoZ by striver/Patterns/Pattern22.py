n= 4
for i in range(2*n-1):
    for j in range(2*n-1):
        top = i
        left = j
        right = (2*n-2)-j
        down=(2*n-2)-i
        m = min(right,left,down,top)
        print(n-m,end=" ")
    print(" ")    