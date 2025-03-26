from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = [col for row in grid for col in row]
        arr.sort()
        midpoint = len(arr) // 2
        ops = 0
        for each in arr:
            if (each - arr[midpoint]) % x != 0:
                return -1
            ops += abs(each - arr[midpoint]) // x
        return ops
    

soln = Solution()
print(soln.minOperations([[2,4],[6,8]], 2))
print(soln.minOperations([[1,5],[2,3]], 1))
print(soln.minOperations([[1,2],[3,4]], 2))
