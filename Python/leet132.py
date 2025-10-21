def findMin(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low+high)//2
        if(nums[mid] > nums[high]):
            low = mid+1
        else:
            high = mid
    return nums[low]
                
my_list1 = [3,4,5,1,2]
my_list2 = [4,5,6,7,0,1,2]
my_list3 = [11,13,15,17]

print(findMin(my_list1))
print(findMin(my_list2))
print(findMin(my_list3))