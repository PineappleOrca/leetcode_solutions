def threeSum(n):
    my_var = n // 3
    my_var_left = my_var - 1
    my_var_right = my_var + 1
    total = my_var_left + my_var + my_var_right 
    if total == n:
        return [my_var_left, my_var, my_var_right]
    else:
        return []
    
def unit_tests():
    tests = [
        (33, [10,11,12]),
        (4, []),
        (12, [3,4,5]),
        (13, [])
    ]
    for test in tests:
        my_var = threeSum(test[0])
        if my_var == test[1]:
            print(f"Test case {test[0]} PASSED with values {my_var}")
        else:
            print(f"Test case {test[0]} FAILED")


unit_tests()