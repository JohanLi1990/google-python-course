from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        num_distinct = 0
        seen={}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        j = 0
        map={}
        ans = 0
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
            while len(map.keys()) == len(seen.keys()):
                ans += len(nums) - i
                map[nums[j]] -= 1
                if map[nums[j]] == 0:
                    del map[nums[j]]
                j += 1
        return ans
    
soln = Solution()
print(soln.countCompleteSubarrays([1,3,1,2,2])) 
print(soln.countCompleteSubarrays( [5,5,5,5])) 