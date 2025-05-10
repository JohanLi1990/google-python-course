from typing import Counter, List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        count1_zero = 0
        count2_zero = 0
        for num in nums1:
            if num == 0:
                count1_zero += 1
        for num in nums2:
            if num == 0:
                count2_zero += 1
        min_sum = max(count1_zero + sum1, count2_zero + sum2)
        if (min_sum - sum1 > 0 and count1_zero == 0 ) or (min_sum - sum2 > 0 and count2_zero == 0):
            return -1
        return min_sum
    
soln = Solution()
print(soln.minSum([3,2,0,1,0], [6,5,0]))
print(soln.minSum([2,0,2,0], [1,4]))
print(soln.minSum([8,13,15,18,0,18,0,0,5,20,12,27,3,14,22,0], [29,1,6,0,10,24,27,17,14,13,2,19,2,11]))