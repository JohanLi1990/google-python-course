from ast import Try
import heapq
from shutil import move
from typing import List

from sympy import true


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # dp[i][j] = max(moveTime[i][j] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        N, M = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * M for _ in range(N)]
        dist[0][0] = 0  # Starting point
        pq = [(0, 0, 0)]
        directions =[-1, 0, 1, 0, -1]
        while pq:
            cost, x, y = heapq.heappop(pq)
            if (x,y) == (N - 1, M -1):
                return cost
            for d in range(4):
                nx, ny = x + directions[d], y + directions[d + 1]
                if 0 <= nx < N and 0 <= ny < M:
                    new_cost = max(cost + 1, moveTime[nx][ny] + 1)
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))
        return -1

soln = Solution()
print(soln.minTimeToReach([[0,4],[4,4]]))
print(soln.minTimeToReach([[0,0,0],[0,0,0]]))
print(soln.minTimeToReach([[15,58],[67,4]]))
print(soln.minTimeToReach([[94,79,62,27,69,84],[6,32,11,82,42,30]]))