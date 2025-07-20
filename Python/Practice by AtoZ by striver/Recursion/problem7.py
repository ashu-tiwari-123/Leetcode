string = input("Enter the String: ")
print(f"String: {string}")
l = len(string)
# Single pointer method
def pallindrome(i,string):
    if(i>=l//2):return True
    if(string[i]!=string[l-i-1]):return False
    return pallindrome(i+1,string)
x=pallindrome(0,string)
print(x)