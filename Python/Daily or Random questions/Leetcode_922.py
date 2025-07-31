# sort array by parity

nums = [4,2,5,7]

n = len(nums)
even =0
odd =1
res = [0]*n

for i in nums:
    if i %2==0:
        res[even] = i
        even+=2
    else:
        res[odd] = i
        odd+=2    

print(res)