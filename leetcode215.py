import heapq

def findKthLargest(nums,k):
    # start with a guess or lowest 0
    # iterate over k in a while loop
    # keep a counter of highest value 
    # find the largest value int he nums list
    # pop it 
    # increment the counter
    # repeat the process till you reach the kth largest value

    # the solution works but takes too long hav eot find something faster
    #sorting is an O(nlogn) algorithm
    # min heaps would be O()
    guess = 0
    my_list = []
    while len(my_list) < k:
        guess = 0
        for item in nums:
            if(item > guess):
                guess = item
        my_list.append(guess)
        nums.remove(guess)
    return my_list[k-1]
nums = [3,2,1,5,6,4]
nums2 = [3,2,3,1,2,4,5,5,6]

print(findKthLargest(nums,2))
print(findKthLargest(nums2,4))