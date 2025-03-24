from typing import List
from heapq import heappush, heappop

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007
        graph = [[] for _ in range(n)]
        for road in roads:
            u, v, w = road[0], road[1], road[2]
            graph[u].append((v, w))
            graph[v].append((u, w))
        # print(graph)
        # Use Dijkstra algorithm
        shortest_time = [float('inf')] * n
        q = [(0, 0)]
        path_count = [0] * n
        path_count[0] = 1
        shortest_time[0] = 0
        while q:
            cur_time, cur_node = heappop(q)
            if cur_time > shortest_time[cur_node]:
                continue
            
            for neighbour, road_time in graph[cur_node]:
                if road_time + cur_time < shortest_time[neighbour]:
                    shortest_time[neighbour] = road_time + cur_time
                    path_count[neighbour] = path_count[cur_node]
                    heappush(q, (shortest_time[neighbour], neighbour))
                elif road_time + cur_time == shortest_time[neighbour]:
                    path_count[neighbour] = (path_count[neighbour] + path_count[cur_node]) % MOD
        return path_count[n - 1]
            


soln = Solution()
print(soln.countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))
print(soln.countPaths(2, [[1, 0, 10]]))