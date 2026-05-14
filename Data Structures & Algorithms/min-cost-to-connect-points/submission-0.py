import heapq
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        totalCost = 0
        visited = set()
        heap = [(0, 0)]

        while len(visited) < n:
            cost, node = heapq.heappop(heap)
            if node in visited: continue
            visited.add(node)
            totalCost += cost

            for i in range(n):
                if i not in visited:
                    edge_cost = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                    heapq.heappush(heap, (edge_cost, i))

        return totalCost

        