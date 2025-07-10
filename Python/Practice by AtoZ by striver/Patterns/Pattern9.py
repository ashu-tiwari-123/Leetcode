n= 5 
for i in range(n):
    for s in range(0,n-i-1):
        print(" ",end=" ")    
    for j in range(0,2*i+1):
        print("x",end=" ")
    print('')
for i in range(n):
    for s in range(i):
        print(" ",end=" ")    
    for j in range(0,2*n-1):
        print("x",end=" ")
    n=n-1
    print('')   
