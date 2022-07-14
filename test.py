def has_33(nums):
    for i in range(0,len(nums)-1): # len(nums) = 3 -1 = 2  
        if nums[i:i+2] == [3,3]:
            return True
    return False

print(has_33([1, 3, 3]))