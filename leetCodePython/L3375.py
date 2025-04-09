from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # bag of words
        bag = set()
        minval = float("inf")
        for num in nums:
            bag.add(num)
            minval = min(num, minval)
        if k < minval:
            return len(bag)
        elif k == minval:
            return len(bag) - 1
        return -1
    
soln = Solution()
print(soln.minOperations([5,2,5,4,5], 2))
        
            