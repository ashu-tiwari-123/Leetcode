count=0
def p():
    global count
    if(count==5):
        return
    print("1")
    count=count+1
    p()

p()

