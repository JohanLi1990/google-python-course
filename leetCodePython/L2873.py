from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxSoFar = 0
        curDiff = 0
        ans = 0
        for num in nums:
            ans = max(ans, curDiff * num)
            curDiff = max(curDiff, maxSoFar - num)
            maxSoFar = max(maxSoFar, num)
        return ans
    
soln = Solution()
print(soln.maximumTripletValue([12,6,1,2,7]))
print(soln.maximumTripletValue([1,10,3,4,19]))