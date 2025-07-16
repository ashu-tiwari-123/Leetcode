n = int(input("enter the number: "))
sum = 0
d = n

while(n>0):
    ld = n %10
    sum = sum + (ld**3)
    n = n//10

if d == sum: print("Armstrong")
else : print("Not Armstrong")