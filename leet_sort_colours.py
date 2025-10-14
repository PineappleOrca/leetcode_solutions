def sortColors(nums):
    lowest_value = nums[0]
    idx = 0
    my_var = True
    while (my_var == True):
        if(idx < len(nums)-1):
            if(nums[idx] > nums[idx+1]):
                nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
        idx += 1
        if(idx == len(nums)-1):
            idx = 0 
        my_var = checkList(nums)
        return nums


def checkList(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return True
    return False
        
nums = [2,1,0]
print(sortColors(nums))
