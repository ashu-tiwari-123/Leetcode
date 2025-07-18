n = int(input("enter the number: "))
rev_num = 0
while(n>0):
    ld = n %10
    print(ld)
    rev_num = (rev_num*10)+ld
    print(rev_num)
    n = n//10

print(rev_num)