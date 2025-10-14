def mergeAlternately(word1, word2):
    my_string = ""
    len1 = len(word1)
    len2 = len(word2)
    iter_len = min(len1,len2)
    print(iter_len)
    for i in range(iter_len):
        my_string += word1[0]
        my_string += word2[0]
        word1 = word1[1:]
        word2 = word2[1:]
    if len(word1) > 0:
        my_string = my_string + word1
    else:
        my_string = my_string + word2
    return my_string

my_string = 'Marina'
my_string2 = 'Kevin'
print(mergeAlternately(my_string, my_string2))