from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        j = 0
        seen = {}
        curk = 0
        ans = 0
        N = len(nums)
        for i in range(N):
            if nums[i] in seen:
                curk += seen[nums[i]]
            seen[nums[i]] = seen.get(nums[i], 0) + 1
            while curk >= k:
                ans +=  N - i
                seen[nums[j]] -= 1
                curk -= seen[nums[j]]
                if seen[nums[j]] == 0:
                    seen.pop(nums[j])
                j += 1
        return ans

soln = Solution()
print(soln.countGood( [1,1,1,1,1], 10))
print(soln.countGood( [3,1,4,3,2,2,4], 2))