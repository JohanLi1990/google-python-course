from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        count = 0
        res = 0
        N = len(nums)
        j = 0
        for i in range(len(nums)):
            if nums[i] == max_num:
                count += 1
            while count >= k:
                res += N - i
                if nums[j] == max_num:
                    count -= 1
                j += 1
        return res

soln = Solution()
print(soln.countSubarrays([1,3,2,3,3], 2)) 
print(soln.countSubarrays([1,4,2,1], 3))