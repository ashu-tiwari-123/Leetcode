n = int(input("Enter the number: "))

def number(i,n):
    if(i>n):
        return
    number(i+1,n)
    print(i)

number(1,n)
