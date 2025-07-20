n = int(input("Enter the number: "))

# Parameterized 
# def sumN(i,sum):
#     if(i<1):
#         print(sum)
#         return
#     sumN(i-1,sum+i)

# Functional 
def sumN(n):
    if(n==0):
        return 0
    return n+sumN(n-1)

res= sumN(n)
print(res)
