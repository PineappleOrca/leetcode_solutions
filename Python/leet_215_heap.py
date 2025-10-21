import heapq

def findKthLargest(nums,k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

# This uses a min heap which is an O(nlog(k)) algorithm
# How this solution works is it makes a minimum heap where the lowest value is on the top and hte highest
# is at the bottom.
# when the length of the heap is too large we pop the smallest value from that list 
# if we find a larger item it gets addedd to the heap
# once it is done we return the nth largest value which should be at the top of the min heap