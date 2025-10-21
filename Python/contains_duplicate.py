def contains_duplicate(my_list):
    my_set = set(my_list)
    if len(my_set) == len(my_list):
        return False
    else:
        return True

my_list = [1,2,3,1]
my_list = [1,2,3,4]

print(contains_duplicate(my_list))
