# sort array by parity

nums = [4,2,5,7]

n = len(nums)
even =0
odd =n/2
res = [0]*n

for i in nums:
    if i %2==0:
        res[even] = i
        even+=1 

print(res)