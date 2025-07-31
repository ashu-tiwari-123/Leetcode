nums =[1,2,3,4,5,1]
nums.sort()

def duplicate(nums):
    for i in range(len(nums)-1):
        if(nums[i]==nums[i+1]):
            return True
    return False 

res=duplicate(nums)
print(res)