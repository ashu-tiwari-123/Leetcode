# 3423. Maximum Difference Between Adjacent Elements in a Circular Array

def maxAdjacentDistance(nums):
    n=[]
    l = len(nums)
    for i in range(0,l-1):
        if(nums[i+1]==l-1):
            n.append(abs(nums[i]-nums[l-1]))
        n.append(abs(nums[i]-nums[i+1]))
    print(n)    
    return max(n)

l = [2,1,0]       
print(maxAdjacentDistance(l))