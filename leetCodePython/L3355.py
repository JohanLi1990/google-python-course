from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        diff = [0] * (N + 1)
        for q in queries:
            diff[q[0]] += 1
            diff[q[1] + 1] -= 1
        curdiff = 0
        for i in range(N):
            curdiff += diff[i]
            if curdiff < nums[i]:
                return False
        return True
    
soln = Solution()
print(soln.isZeroArray([1,0,1], [[0,2]]))
print(soln.isZeroArray([4,3,2,1], [[1,3],[0,2]]))