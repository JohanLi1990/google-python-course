from typing import List

class Solution:
    
    def countPairs(self, nums: List[int], k: int) -> int:
        '''
        what N**2 is not good enough, 
        can we make use of gcd to do this?
        '''
        count = [[] for _ in range(101)] # num -> List[index]
        ans = 0
        for i, num in enumerate(nums):
            for j in count[num]:
                if (j * i) % k == 0:
                    ans += 1
            count[num].append(i)
        return ans    
        
        
    
soln = Solution()
print(soln.countPairs( [3,1,2,2,2,1,3], 2)) #4
print(soln.countPairs([1,2,3,4], 1)) #0
print(soln.countPairs([10,2,3,4,9,6,3,10,3,6,3,9,1], 4)) #8
print(soln.countPairs([2,5,10,5,2,2,5], 9)) #3
                