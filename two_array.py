def searchMatrix(matrix, target):
    my_list = [element for sublist in matrix for element in sublist]
    left, right = 0, len(my_list)-1
    while left <= right:
        mid = left + (right-left)//2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            left = mid+1
        else:
            right = mid - 1
    return False


array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(searchMatrix(array_2d, 4))
