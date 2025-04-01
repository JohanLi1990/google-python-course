from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        
        def dfs(index:int) -> int:
            if (index >= len(questions)): 
                return 0
            if dp[index] != 0:
                return dp[index]
            take, no_take =0, 0
            take = questions[index][0] + dfs(index + questions[index][1] + 1)
            no_take = dfs(index + 1)
            dp[index] = max(take, no_take)
            return dp[index]
        
        return dfs(0)

soln = Solution()
print(soln.mostPoints( [[3,2],[4,3],[4,4],[2,5]])) # 5
print(soln.mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]])) # 7
