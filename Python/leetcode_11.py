def maxArea(height):
    left, right = 0,len(height)-1
    max_area = 0
    while left < right:
        my_area = (right - left)*(min(height[right],height[left]))
        max_area = max(my_area,max_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))



