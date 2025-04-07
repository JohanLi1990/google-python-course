from tkinter.tix import Tree
from typing import List

from sympy import false


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        dp = [0] * (total + 1)
        dp[0] = 1
        for num in nums:
            for i in range(len(dp) - 1, -1, -1):
                if dp[i] > 0:
                    dp[i + num] += 1
                    if i + num == total / 2:
                        return True
        return False
    
soln = Solution()
print(soln.canPartition([1,5,11,5]))
print(soln.canPartition([1,2,3,5]))