from collections import Counter
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    my_output = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in my_output:
            my_output[key] = []
        my_output[key].append(word)
    return list(my_output.values())
        
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))