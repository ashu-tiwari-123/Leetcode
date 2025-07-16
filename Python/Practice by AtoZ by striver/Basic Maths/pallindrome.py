n = int(input("enter the number: "))
rev_num = 0
d = n

while(n>0):
    ld = n %10
    rev_num= (rev_num*10)+ld
    n = n //10

if d == rev_num : print("Pallindrome")
else : print("Not Pallindrome")