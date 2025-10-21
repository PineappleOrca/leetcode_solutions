def trap(height):
    left, right = 0, 1
    while left < right:
        middle = height[right-left]
        if(height[left] >= middle) & (height[right] >= middle):
            my_area += 
