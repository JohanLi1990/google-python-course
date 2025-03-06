class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        curSet = set()
        ans = []
        sum = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] in curSet:
                    ans.append(grid[i][j])
                sum += grid[i][j]
                curSet.add(grid[i][j])
        diff = sum - (1 + n**2) * (n**2) / 2    
        ans.append(int(ans[0] - diff))
        return ans

soln = Solution()
print(soln.findMissingAndRepeatedValues([[1,3],[2,2]]))         