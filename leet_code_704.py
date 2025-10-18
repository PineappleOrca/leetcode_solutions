def search(nums: list[int], target:int)-> int:
    # This is the function which returns the value without using a binary search
    if target in nums:
        return nums.index(target)
    else:
        return -1

def binarySearch(nums: list[int], target:int) -> int:
    # this is the function with the algorithm for the binary search    
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right)//2
        if(nums[mid] == target):
            return mid
        elif(nums[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return -1


def unit_test(tests: list):
    i= 0
    for test in tests:
        my_var = binarySearch(test[0], test[1])
        if(my_var == test[2]):
            print(f"Unit Tests: {i} PASSED")
            i += 1
        else:
            print(f"Unit Tests: {i} FAILED with Result {my_var} and Expected: {test[2]}")
            i += 1

unit_tests = [
    [[-1,0,3,5,9,12],9,4],
    [[-1,0,3,5,9,12],2,-1]
]

unit_test(unit_tests)
