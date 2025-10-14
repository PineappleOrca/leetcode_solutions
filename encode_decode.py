def encode(strs):
    my_string = ""
    for word in strs:
        my_string += word + " "
    return my_string

def decode(s):
    if s == "":
        return [""]
    else:
        return s.split()



