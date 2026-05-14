import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap =  [-1 * val for val in count.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0

        while heap or queue:
            time += 1
            if heap:
                count = heapq.heappop(heap)
                count += 1
                if count < 0:
                    queue.append((count, time + n))

            if queue and queue[0][1] == time:
                count, _ = queue.popleft()
                heapq.heappush(heap, count)


        return time
    





        
        



        
            

        