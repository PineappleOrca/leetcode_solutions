def isIsomorphic(s, t):
    my_s = assemble(s)
    my_t = assemble(t)
    if my_s == my_t:
        return True
    else:
        return False
    

def createDict(my_string):
    return {key: 0 for key in my_string}

def findCount(my_string, my_dict):
    for letter in my_string:
        if letter in my_dict:
            my_dict[letter] += 1
    return my_dict

def getValues(my_dict):
    return list(my_dict.values())

def assemble(my_string):
    my_dict = createDict(my_string)
    my_count = findCount(my_string, my_dict)
    my_values = getValues(my_count)
    return sorted(my_values)

print(isIsomorphic('add', 'bar'))