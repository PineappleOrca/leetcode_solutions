class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_counter = 0
        for idx, num in enumerate(my_set):
            if num-1 not in my_set:
                my_counter = 1
                i = idx + 1
                my_test = num+1
                while True:
                    if my_test in my_set:
                        my_counter += 1
                        my_test += 1
                    else:
                        break
                max_counter = max(my_counter, max_counter)
        return max_counter        