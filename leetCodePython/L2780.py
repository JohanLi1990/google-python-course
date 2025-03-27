from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # find the most dominant mem
        count, cand = 0, 0
        curDict = {}
        for num in nums:
            curDict[num] = curDict.get(num, 0) + 1
            if count == 0:
                cand = num
            count += (1 if num == cand else -1)
        
        first = 0
        rest = curDict[cand]
        for i in range(len(nums)):
            if nums[i] == cand:
                first += 1
                
            rest = curDict[cand] - first
            if (first > (i + 1) // 2) and (rest > (len(nums) - i - 1)//2):
                return i
                        
        return -1
    
soln = Solution()
print(soln.minimumIndex([1,2,2,2]))
print(soln.minimumIndex([2,1,3,1,1,1,7,1,2,1]))