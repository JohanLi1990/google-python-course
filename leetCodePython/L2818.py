import heapq
import math
from typing import List

class Solution:
    MOD = 1_000_000_007
                   
    def _power(self, base:int, exponent:int) -> int:
        res = 1
        while exponent > 0:
            if exponent % 2 == 1:
                res = (res * base) % self.MOD
            base = (base * base) % self.MOD
            exponent //= 2
        return res
        
    def _primeScore(self, num: int) -> int:
        count = 0
        for factor in range(2, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                count += 1
                while num % factor == 0:
                    num //= factor
        if num >= 2:
            count  += 1
        return count
        
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)]
        arr.sort(key=lambda o:(-o[0], o[1]))
        # print(arr)
        self.sieve = [0] * len(nums)
        for i, num in enumerate(nums):
            self.sieve[i] = self._primeScore(num)
            
        ans = 1
        # print(self.sieve[40:100])
        monostack = []
        prevDom = [i for i in range(N)] 
        nextDom = [N for i in range(N)]
        for i, num in enumerate(nums):
            while monostack and self.sieve[monostack[-1]] < self.sieve[i]:
                nextDom[monostack.pop()] = i
            prevDom[i] = monostack[-1] if monostack else -1
            monostack.append(i)
        
        for localMax in arr:
            curMax, curIndex = localMax[0], localMax[1]
            l, r = prevDom[curIndex], nextDom[curIndex]
            curCombinations = (curIndex - l) * (r - curIndex)
            if curCombinations >= k:
                #  pow function is expensive
                # ans = (ans * pow(curMax, k, MOD)) % MOD
                ans = (ans * self._power(curMax, k)) % self.MOD
                return ans
            # ans = (ans * pow(curMax, curCombinations, MOD)) % MOD
            ans = (ans * self._power(curMax, curCombinations)) % self.MOD
            # ans %= MOD
            k -= curCombinations

        return -1
    
    # def maximumScore(self, nums: List[int], k: int) -> int:
         
    #     arr = [[v, i] for i, v in enumerate(nums)]
    #     arr.sort(key=lambda o:(-o[0], o[1]))
    #     # print(arr)
    #     MOD = 1_000_000_007
    #     ans = 1
    #     # print(self.sieve[40:100])
    #     for localMax in arr:
    #         curMax, curIndex = localMax[0], localMax[1]
    #         l, r = curIndex, curIndex
    #         curPrimeScore = self.sieve[curMax]
    #         #  this part is not efficient
    #         while l > 0 and self.sieve[nums[l - 1]] < curPrimeScore:
    #             l -= 1
    #         while r < len(nums) - 1 and self.sieve[nums[r + 1]] <= curPrimeScore:
    #             r += 1
    #         curCombinations = max(1, curIndex - l + 1) * max(1, r - curIndex + 1)
    #         if curCombinations >= k:
    #             ans = (ans * pow(curMax, k, MOD)) % MOD
    #             # ans %= MOD
    #             return ans
    #         ans = (ans * pow(curMax, curCombinations, MOD)) % MOD
    #         # ans %= MOD
    #         k -= curCombinations

    #     return -1
    
soln = Solution()
print(soln.maximumScore([8,3,9,3,8], 2))
print(soln.maximumScore([19,12,14,6,10,18], 3))
print(soln.maximumScore([3289,2832,14858,22011], 6)) # 256720975