import heapq
from multiprocessing import heap
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # Dijkstra algorithm.
        N, M = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * M for _ in range(N)  ]
        dist[0][0] = 0
        dirs = [-1, 0, 1, 0, -1]
        pq = [(0, 0, 0, 0)] # cost, step, x, y
        step = 0
        while pq:
            cost, step, x, y = heapq.heappop(pq)
            if x == N - 1 and y == M - 1:
                return cost
            for d in range(4):
                nx, ny = x + dirs[d], y + dirs[d + 1]
                if 0 <= nx < N and 0 <= ny < M:
                    ncost = max(1 + step % 2 + cost, moveTime[nx][ny] + step % 2 + 1)
                    if ncost < dist[nx][ny]:
                        dist[nx][ny] = ncost
                        heapq.heappush(pq, (ncost, step + 1, nx, ny))
        return  -1

soln = Solution()
print(soln.minTimeToReach([[0,4],[4,4]]))
print(soln.minTimeToReach([[0,0,0,0],[0,0,0,0]]))
print(soln.minTimeToReach([[0,1],[1,2]]))
        