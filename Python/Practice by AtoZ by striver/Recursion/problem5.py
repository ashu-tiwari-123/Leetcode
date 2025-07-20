n = int(input("Enter the number: "))

# Functional 
def fact(n):
    if(n==0 or n==1):
        return 1
    return n * fact(n-1)

res= fact(n)
print(res)
