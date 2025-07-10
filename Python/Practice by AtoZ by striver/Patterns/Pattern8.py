n= 5 
for i in range(n):
    for s in range(i):
        print(" ",end=" ")    
    for j in range(0,2*n-1):
        print("x",end=" ")
    n=n-1
    print('')