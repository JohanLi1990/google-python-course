from itertools import accumulate
from typing import List


class Solution:
    
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = list(accumulate(nums))
        N  = len(nums)
        if prefix_sum[-1] * N < k:
            return N * (N + 1) // 2
        j = 0
        res = 0
        for i in range(len(nums)):
            curval = prefix_sum[i] * (i - j + 1)
            if curval >= k:
                lo, hi = j, i
                while(lo < hi):
                    mid = lo + (hi - lo) // 2
                    bottom = 0 if mid < 1 else prefix_sum[mid - 1]
                    cur_product = (prefix_sum[i] - bottom) * (i - mid + 1)
                    if cur_product >= k:
                        lo = mid + 1
                    else:
                        hi = mid 
                j = lo
            res += i - j + 1 if nums[j] < k else 0
        return res

soln = Solution()
# print(soln.countSubarrays([2,1,4,3,5], 10))
print(soln.countSubarrays([9,5,3,8,4,7,2,7,4,5,4,9,1,4,8,10,8,10,4,7], 4))