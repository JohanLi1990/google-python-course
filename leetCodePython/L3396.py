import re
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = {}
        lastRepeating = 0
        for i in range(len(nums) - 1, -1, -1):
            count[nums[i]] = count.get(nums[i], 0) + 1
            if count[nums[i]] > 1:
                lastRepeating = i + 1
                break
            
        # we need to at least remove the first lastRepeatIndex items
        ans = lastRepeating // 3
        if lastRepeating % 3 == 0:
            return ans
        else:
            return ans + 1
    
soln = Solution()
print(soln.minimumOperations( [1,2,3,4,2,3,3,5,7]))
print(soln.minimumOperations( [4,5,6,4,4]))
print(soln.minimumOperations( [6, 7, 8, 9]))
print(soln.minimumOperations( [3, 7, 7, 3]))
print(soln.minimumOperations([2,7,15,1,15]))
        