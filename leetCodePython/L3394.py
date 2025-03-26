from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        def checkaxis(ranges: List[List[int]]) -> bool:
            ranges.sort(key=lambda o: (o[0], o[1]))
            prev = -1
            ans = 0
            for intv in ranges:
                if intv[0] >= prev:
                    ans += 1
                prev = max(prev, intv[1])
                if ans >= 3:
                    return True
            return ans == 3
            
        x_axis = [[l[0], l[2]] for l in rectangles]
        if checkaxis(x_axis):
            return True
        else:
            return checkaxis([[l[1], l[3]] for l in rectangles])
        
soln = Solution()
print(soln.checkValidCuts(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
print(soln.checkValidCuts(4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))
print(soln.checkValidCuts(4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))