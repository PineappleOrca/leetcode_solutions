def sortArray(nums):
    my_nums = list(set(nums))
    my_sorted_list = []
    my_var = 0
    while len(nums) > 0:
        current_var = nums[my_var] 
        lowest = min()
        
