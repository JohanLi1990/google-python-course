from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        maxdiff, mindiff = 0, 0
        cur = 0
        for diff in differences:
            cur += diff
            maxdiff = max(maxdiff, cur)
            mindiff = min(mindiff, cur)
            
        # the interval
        lowbound = lower - mindiff
        highbound = upper - maxdiff
        return max(0, highbound - lowbound + 1)

soln = Solution()
print(soln.numberOfArrays([1,-3,4], 1, 6))
print(soln.numberOfArrays([3,-4,5,1,-2], -4, 5))
print(soln.numberOfArrays([4, -7, 2], 3, 6))
print(soln.numberOfArrays([-40], -46, 53))