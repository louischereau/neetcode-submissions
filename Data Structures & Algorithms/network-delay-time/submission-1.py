import heapq
import math 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        dist = {key: float(math.inf) for key in range(1, n+1) if key != k}
        dist[k] = 0
        queue = []
        heapq.heappush(queue, [k, 0])

        adj = {}

        for i in range(1, n+1):
            adj[i] = [(time[1], time[2]) for time in times if time[0] == i]

        while queue:
            node, time = heapq.heappop(queue)
            
            if time > dist[node]: continue

            for neighbor, ng_time in adj[node]:
                if dist[node] + ng_time < dist[neighbor]:
                    dist[neighbor] = dist[node] + ng_time
                    heapq.heappush(queue, [neighbor, dist[neighbor]])

        print(dist)

        for node, time in dist.items():
            if time == math.inf:
                return -1

        return max(dist.values())
        