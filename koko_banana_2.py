import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        min_rate, max_rate = 1,max(piles)
        result = max_rate
        while min_rate <= max_rate:
            mid = (min_rate + max_rate) // 2
            if(self.compute_eating(piles, mid) <= h):
                result = mid
                max_rate = mid - 1
            else:
                min_rate = mid + 1
        return result
    
    def compute_eating(self, piles, mid):
        return sum(math.ceil(float(p)/mid) for p in piles)
