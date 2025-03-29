from asyncio import FastChildWatcher
from calendar import c
from collections import deque
import heapq
from typing import List


class Solution:
    dir = [-1, 0, 1, 0, -1]
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        M , N = len(grid), len(grid[0])
        qs = [[v, i]  for i, v in enumerate(queries)]
        qs.sort(key=lambda o:[o[0], o[1]])
        
        #  for each query, use the last layer of the previous query
        # do bfs based on the last layer, and count how many items have been acquired, 
        # return the number of items covered, and upadte the last layer as a side effect
        lastLayer = deque([0])
        prev = 0
        visited = [False] * N * M
        def bfs(qVal:int, queue:deque) -> int:
            accum = 0
            nextLayer = deque()
            while queue:
                curPoint = queue.popleft()
                curX = curPoint // N
                curY = curPoint % N
                curVal = grid[curX][curY]
                if curVal >= qVal:
                    nextLayer.append(curPoint)
                    continue
                visited[curPoint] = True
                accum += 1
                for i in range(len(self.dir) - 1):
                    nextX = curX + self.dir[i]
                    nextY = curY + self.dir[i + 1]
                    if nextX < 0 or nextY < 0 or nextX >=M or nextY >= N or visited[nextX * N + nextY]:
                        continue
                    queue.append(nextX * N + nextY)
                    visited[nextX * N + nextY] = True
            return accum, nextLayer
                    
        ans = [0] * len(queries)
        for i in range(len(qs)):
            curQuery = qs[i]
            if i > 0 and qs[i][0] == qs[i - 1][0]:
                ans[curQuery[1]] = ans[qs[i - 1][1]]
                continue
            gained, lastLayer = bfs(curQuery[0], lastLayer)
            ans[curQuery[1]] = prev + gained
            prev = ans[curQuery[1]]
        return ans
    
    # Better solution, using minHeap, it is a queue anyway... 
    # why didn't I think of it...
    def maxPointsII(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        min_heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        points = 0
        
        # Sort queries and keep track of original indices
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        result = [0] * len(queries)
        
        for query, original_index in sorted_queries:
            while min_heap and min_heap[0][0] < query:
                _, x, y = heapq.heappop(min_heap)
                points += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        heapq.heappush(min_heap, (grid[nx][ny], nx, ny))
            result[original_index] = points
        
        return result
        

soln = Solution()
print(soln.maxPoints([[1,2,3],[2,5,7],[3,5,1]], [5,6,2]))
print(soln.maxPoints([[5,2,1],[1,1,2]], [3]))