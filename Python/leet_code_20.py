def isValid(s: str) -> bool:
    my_mapping = {'(':')', '[':']', '{':'}'} 
    my_stack = []
    for char in s:
        if char in my_mapping:
            top_element = my_stack.pop()
            if my_mapping[char] != top_element:
                return False
        else:
            my_stack.append(char)
    return not my_stack
    
s = "()"
print(isValid(s))