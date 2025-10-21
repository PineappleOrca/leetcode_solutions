def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

def unit_test():
    unit_tests = [
        ["abcabcbb",3],
        ["bbbbb",1],
        ["pwwkew", 3],
        ["aab", 2]
    ]
    number = 0
    for test in unit_tests:
        output = lengthOfLongestSubstring(test[0])
        if output == test[1]:
            print(f"Unit Test {number+1}: PASSED")
        else:
            print(f"Unit Test {number+1} FAILED with Output: {output} and Expected: {test[1]}")

unit_test()