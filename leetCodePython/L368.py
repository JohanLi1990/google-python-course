from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        largest = -1
        ans = 1
        for i in range(len(nums)):
            curans = 1
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j]  == 0:
                    if dp[j] + 1 > curans:
                        curans = dp[j] + 1
                        prev[i] = j
            if curans > ans:
                ans = curans
                largest = i
            dp[i] = curans
        ret = []
        while largest >= 0:
            ret.append(nums[largest])
            largest = prev[largest]
        if not ret:
            return [nums[0]]
        return ret

soln = Solution()
print(soln.largestDivisibleSubset([1,2,3]))
print(soln.largestDivisibleSubset([1,2,4,8]))
                