from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        j = 0
        seen = {0:1}
        res = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % modulo == k:
                count += 1
            cur_count_mod = count % modulo
            deduct = (cur_count_mod + modulo - k) % modulo
            res += seen.get(deduct, 0)
            seen[cur_count_mod] = seen.get(cur_count_mod, 0) + 1
        return res
    
soln = Solution()
print(soln.countInterestingSubarrays([3, 2, 4], 2, 1))
print(soln.countInterestingSubarrays([3, 1, 9, 6], 3, 0))
            