# 136. Single Number

def singleNumber(nums):
    nums.sort()
    for i in nums:
        if (nums.count(i)>=2):
            nums.remove(i)
        else:
            return i    

list = [2,2,1]
print(singleNumber(list))