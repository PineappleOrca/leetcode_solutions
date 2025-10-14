def longestConsecutive(nums):
    my_keys = list(set(nums))
    longest = 0
    for key in my_keys:
        if ((key+1) in my_keys):
            if ((key-1) in my_keys):
                longest+=1
    my_dict = dict.fromkeys(nums)
    print(longest+2)

longestConsecutive([1,0,1,2])