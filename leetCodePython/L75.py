from typing import List

from sympy import solve, true


class Solution:
    def swap(self, arr: List[int], i, j):
        arr[i] = arr[i] + arr[j]
        arr[j] = arr[i] - arr[j]
        arr[i] = arr[i] - arr[j]
        
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        s, e = 0, N - 1
        print(nums)
        for i in range(N):
            # compare with p
            while True:
                if nums[i] == 0 and i > s:
                    self.swap(nums, i, s)
                    s += 1
                elif nums[i] == 2 and i < e:
                    self.swap(nums, i, e)
                    e -= 1
                else:
                    break
                
soln = Solution()
ans = [1, 0,2 , 1, 2, 0, 2]
print(soln.sortColors(ans))
print(ans)