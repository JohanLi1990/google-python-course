from typing import List
import heapq

class Solution:
    # def putMarblesII(self, weights: List[int], k: int) -> int:
    #     N = len(weights)
    #     dp_max = [[-1] * N for _ in range(k)]
    #     dp_min = [[-1] * N for _ in range(k)]
    #     # dp[k][0] is the answer
    #     def dfs(index: int, curK: int) -> tuple:
    #         if curK == 0:
    #             return (weights[index] + weights[N - 1], weights[index] + weights[N - 1])
    #         if dp_max[curK][index] != -1:
    #             return dp_max[curK][index], dp_min[curK][index]
    #         localMax, localMin = float('-inf'), float('inf')
    #         for i in range(index, N - curK):
    #             curScore = weights[i] + weights[index]
    #             subScore = dfs(i + 1, curK - 1)
    #             localMax = max(localMax, curScore + subScore[0])
    #             localMin = min(localMin, curScore + subScore[1])
    #         dp_max[curK][index] = localMax
    #         dp_min[curK][index] = localMin
    #         return localMax, localMin
    #     res = dfs(0, k - 1)
    #     return res[0] - res[1]
    
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairWeights = []
        N = len(weights)
        for i in range(N - 1):
            pairWeights.append(weights[i] + weights[i + 1])
        pairWeights.sort()
        # top k -1 splits and min k - 1 splits
        ans = 0
        for top, bottom in zip(pairWeights[:k - 1], pairWeights[1 - k:]):
            # print(f'min: {top}, max: {bottom}')
            ans += bottom - top
        return ans

soln = Solution()
print(soln.putMarbles([1, 3, 5, 1], 2))
print(soln.putMarbles([1, 3], 2))