def productExceptSelf(nums: list[int]) -> list[int]:
    # Creating a reversed copy for the right pass to iterate forward
    my_nums = nums[::-1]
    #initialising the first part of the lsits as 1
    left_pass, right_pass = [1], [1]
    # left pass 
    for i in range(1,len(nums)):
        # left pass calculation
        left_pass.append(left_pass[i-1]*nums[i-1])
        # right pass calculation
        right_pass.append(right_pass[i-1]*my_nums[i-1])
    # reversing the right_pass to get the multipications
    right_pass.reverse()
    my_list = []
    # appending the calculations
    for i in range(len(nums)):
        my_list.append(left_pass[i]*right_pass[i])
    return my_list


