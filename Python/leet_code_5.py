def longestPalindrome(s):
    left, right = 0, 2 
    my_string = ""
    max_len = 0
    for char in s:
        while right < len(s):
            test_string = s[left:right]
            my_check = checkPalindrome(test_string)
            if(my_check == True):
                max_len = max(max_len, len(test_string))
            right += 2
    return max_len

def checkPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False 

def unit_tests():
    unit_tests = [
        ["abcabcbb",3],
        ["bbbbb",1],
        ["pwwkew", 3],
        ["aab", 2]
    ]
    number = 0
    for test in unit_tests:
        output = longestPalindrome(test[0])
        if output == test[1]:
            print(f"Unit Test {number+1}: PASSED")
        else:
            print(f"Unit Test {number+1} FAILED with Output: {output} and Expected: {test[1]}")
        number += 1

unit_tests()