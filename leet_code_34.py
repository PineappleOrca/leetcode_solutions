def searchRange(nums: list[int], target: int) -> list[int]:
    '''
    This is the solution to the LeetCode problem number 34
    Finding the first and last position of the elemetn in the sorted array
    if the taget is not in the array return [-1,-1]
    write an algorithm to return the min and max position of the target in O(logn) runtime
    The solution presented here is O(N) not O(log n)
    '''
    if(target not in nums):
    # This returns [-1,-1] since target is not ion nums
        return [-1,-1]
    else:
        # generating a list of elements with the index of target in nums then returning
        my_list = [i for i,x in enumerate(nums) if x==target]
        return [min(my_list), max(my_list)] 

def unit_test_cases(test_cases):
    def decorator(func):
        def wrapper():
            for i,(arg1,arg2,expected) in enumerate(test_cases,1):
                result = func(arg1,arg2)
                if result == expected:
                    print(f"Unit Test {i}: PASSED")
                else:
                    print(f"Unit Test {i}: FAILED with Result: {result} when Expected: {expected}")
        return wrapper
    return decorator

unit_tests = [
    [[5,7,7,8,8,10], 8, [3,4]],
    [[5,7,7,8,8,10], 6,[-1,-1]],
    [[],0,[-1,-1]]
]

# Applying the unit tests
@unit_test_cases(unit_tests)
def run_func(s,t):
    return searchRange(s,t)

run_func()