def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    else: 
        my_string = ""
        my_letters = [letter for letter in strs[0]]
        strs.remove(strs[0])
        my_dict = dict.fromkeys(my_letters, 0)
        print(my_dict)
        for key, var in enumerate(my_dict):
            for word in strs:
                if var in word:
                    
    return my_string

longestCommonPrefix(["flower","flow","flight"])