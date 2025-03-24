from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        prev = 0
        ans = 0
        for meet in meetings:
            ans += max(0, meet[0] - prev - 1)
            prev = max(prev, meet[1])
        
        ans += max(0, days - prev)
        return ans
    
soln = Solution()
print(soln.countDays(10, [[5,7],[1,3],[9,10]]))
print(soln.countDays(5, [[2,4],[1,3]]))
print(soln.countDays(6, [[1,6]]))