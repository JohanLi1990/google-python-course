from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        intervals = [0] * 1001
        N = len(arr)
        ans = 0
        for j in range(N):
            for k in range(j + 1, N):
                if abs(arr[k] - arr[j]) <= b:
                    left = max(0, max(arr[j] - a, arr[k] - c))
                    right = min(1000, min(arr[j] + a, arr[k] + c))
                    if left <= right:
                        if left <= 0:
                            ans += intervals[right]
                        else:
                            ans += intervals[right] - intervals[left - 1]       
            for i in range(arr[j], 1001):
                intervals[i] += 1
        return ans

# soln = Solution()
# print(soln.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3))
# print(soln.countGoodTriplets([1,1,2,2,3], 0, 0, 1))
# print(soln.countGoodTriplets([7,3,7,3,12,1,12,2,3], 5, 8, 1))
            