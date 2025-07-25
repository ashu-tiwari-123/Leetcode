l = [1,2,-1,-2,1,0,-1]

s = set(x for x in l if x>0 or l)
print(s)
total = sum(l)