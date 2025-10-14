from collections import Counter
def isIsomorphic(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    my_dict = {}
    for idx, letter in enumerate(s):
        my_dict[letter] = t[idx]
    my_string = ""
    for letter in s:
        my_string += my_dict[letter]
    has_duplications = len(set(my_dict.values())) < len(my_dict)
    if(has_duplications == True):
        return False
    if(my_string == t):
        return True
    else:
        return False

# Normal function for unit testing 
def unit_tests():
    unit_tests = [
       ["egg", "add",True],
       ["foo", "bar", False],
       ["paper", "title", True],
       ["bbbaaaba", "aaabbbba", False],
        ["badc", "baba", False]
    ]
    number = 0
    for test in unit_tests:
        output = isIsomorphic(test[0], test[1])
        if output == test[2]:
            print(f"Unit Test {number+1}: PASSED")
        else:
            print(f"Unit Test {number+1}: FAILED with Output: {output} and Expected: {test[2]}")
        number += 1

# unit_tests() <- unit testing functiona call

# Decorator to run multiple test cases
def unit_test_cases(test_cases):
    def decorator(func):
        def wrapper():
            for i, (arg1, arg2, expected) in enumerate(test_cases,1):
                result = func(arg1, arg2)
                if result == expected:
                    print(f"Unit Test {i}: PASSED")
                else:
                    print(f"Unit Test {i}: Failed with Output {result} when Expected: {expected}")
        return wrapper
    return decorator

unit_tests = [
       ["egg", "add",True],
       ["foo", "bar", False],
       ["paper", "title", True],
       ["bbbaaaba", "aaabbbba", False],
        ["badc", "baba", False]
    ]

#Applying the decorator to the test cases
@unit_test_cases(unit_tests)
def run_isomorphic_test(s,t):
    return isIsomorphic(s,t)

run_isomorphic_test()