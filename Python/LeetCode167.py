def twoSum(numbers, target):
    #my_numbers = list(set(numbers))
    #my_numbers.sort()
    for index, var in enumerate(numbers):
        total = var + numbers[index+1]
        print(total, index, var)
        if(total == target):
            print(f"I am here, total is {total}, {numbers.index(var)+1} and {numbers.index(numbers[index+1])+1}")
            return [numbers.index(var)+1, numbers.index(var)+2]
        else:
            difference = target - var
            if(difference in numbers):
                return [numbers.index(var)+1, numbers.index(difference)+1]

         
def unit_tests():
    tests = [
       [[2,7,11,15], 9, [1,2]],
        [[2,3,4], 6, [1,3]],
        [[-1,0], -1, [1,2]],
        [[0,0,3,4], 0, [1,2]]
    ]
    for test in tests:
        my_var = twoSum(test[0], test[1])
        print(f"Test case {test[0]} with Target: {test[1]} and answer: {test[2]}")
        if my_var == test[2]:
            print(f"Test case {test} PASSED")
        else:
            print(f"Test case {test[0]} FAILED with answers {my_var} when the target is {test[2]}")

unit_tests()
