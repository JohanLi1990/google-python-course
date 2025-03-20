class Solution(object):
    class DJS:
        '''
        Union find
        '''
        def __init__(self, n):
            self.parent = [i for i in range(n)]
            self.weight = [2**17 - 1] * n
            
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y, w):
            px = self.find(x)
            py = self.find(y)
            
            if px == py:
                self.weight[px] &= w
                return

            if self.weight[px] <= self.weight[py]:
                self.parent[py] = px
                self.weight[px] &= self.weight[py] & w
            else:
                self.parent[px] = py
                self.weight[py] &= self.weight[px] & w
            
        def __str__(self):
            return f"parent: {self.parent}, \n weight: {self.weight}"
    
    def minimumCost(self, n, edges, query):
        """
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """
        dataSet = self.DJS(n)
        for edge in edges:
            dataSet.union(edge[0], edge[1], edge[2])
        
        ans = []
        for q in query:
            u, v = q[0], q[1]
            pu, pv = dataSet.find(u), dataSet.find(v)
            if (pu == pv):
                ans.append(dataSet.weight[pu])
            else:
                ans.append(-1)
        return ans
    
soln = Solution()
print(soln.minimumCost(5, [[0,1,7],[1,3,7],[1,2,1]], [[0,3],[3,4]]))
print(soln.minimumCost(5, [[0,2,7],[0,1,15],[1,2,6],[1,2,1]],  [[1,2]]))
        