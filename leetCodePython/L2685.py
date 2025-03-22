from typing import List

class Solution:
    
    class DJS:
        def __init__(self, n: int):
            self.p = [i for i in range(n)]
            self.w = [0] * n
        
        def find(self, x: int) -> int:
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
        
        def union(self, x, y):
            px = self.find(x)
            py = self.find(y)
            if px == py:
                self.w[px] += 1
                return
            if self.w[px] < self.w[py]:
                self.p[px] = py
                self.w[py] += self.w[px] + 1
            else:
                self.p[py] = px
                self.w[px] += self.w[py] + 1
            
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        dataSet = self.DJS(n)
        for edge in edges:
            dataSet.union(edge[0], edge[1])
        
        group = {}
        for i in range(n):
            pi = dataSet.find(i)
            group[pi] = group.get(pi, 0) + 1
        
        ans = 0
        for k, v in group.items():
            if (v * (v - 1) // 2) == dataSet.w[k]:
                ans += 1
        return ans
    
soln = Solution()
print(soln.countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4]]))
print(soln.countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4],[3,5]]))