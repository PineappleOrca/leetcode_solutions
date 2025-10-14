from collections import Counter

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    else:
        key_1 = getSet(s)
        key_2 = getSet(t)
        if Counter(key_1) == Counter(key_2):
            return True
        else:
            return False

def getSet(my_string):
    my_dict = {}
    for char in my_string:
        print(char)
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    print(my_dict)
    return my_dict 

s = "aacc"
t = "ccac"

print(isAnagram(s,t))
