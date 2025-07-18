n = int(input("Enter the number: "))

# def number(i,n):
#     if(i>n):
#         return
#     print(i)
#     number(i+1,n)

# Using backtracking

def number(i):
    if(i<1):
        return
    number(i-1)
    print(i)

number(n)
