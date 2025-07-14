n=5
for i in range(n):
    for j in range(n-i):
        print("x" , end=" ")
    for s in range(2*i):
        print(" ",end=" ")
    for j in range(n-i):
        print("x" , end=" ")         
    print(' ')
for i in range(n):
    for j in range(i+1):
        print("x",end=" ")
    for s in range(2*n-2):
        print(" ",end=" ")  
    for j in range(i+1):
        print("x",end=" ")
    n=n-1          
    print(' ')    