import math
n = int(input("enter the number: "))
# for i in range(1,n+1):
#     if(n%i==0):print(i)

# Another logic by striver

for i in range(1,int(math.sqrt(n)+1)):
    if(n%i==0):
        print(i)
        if(n/i!=i):print(abs(n/i))