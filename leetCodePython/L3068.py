from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # A XOR B XOR B = A
        # so edges are useless 
        cnt = 0
        for (i, num)  in enumerate(nums):
            nxork = num ^ k
            if nxork > num:
                nums[i] = nxork
                cnt += 1
        if cnt % 2 == 1:
            minDiff, idx = float("inf"), -1
            for (i, num) in enumerate(nums):
                curDiff = abs(num - (num ^ k))
                if curDiff < minDiff:
                    idx = i
                    minDiff = curDiff
            nums[idx] = nums[idx] ^ k
        return sum(nums)
    
soln = Solution()
# print(soln.maximumValueSum([1, 2, 1], 3, [[0,1],[0,2]]))
# print(soln.maximumValueSum([2, 3], 7, [[0,1]]))
print(soln.maximumValueSum([24,78,1,97,44], 6, [[0,2],[1,2],[4,2],[3,4]]))