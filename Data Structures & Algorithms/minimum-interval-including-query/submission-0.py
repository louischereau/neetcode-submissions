import bisect
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = [-1] * len(queries)

        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        sorted_queries = sorted([(query, index) for index, query in enumerate(queries)], key=lambda x: x[0])

        heap = []
        i = 0
        n = len(intervals)
        
        for query, query_index in sorted_queries:

            while i < n and sorted_intervals[i][0] <= query:
                size = sorted_intervals[i][1] - sorted_intervals[i][0] + 1
                end_time = sorted_intervals[i][1]
                heapq.heappush(heap, (size, end_time))
                i += 1
            
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                output[query_index] = heap[0][0]
        
        return output



        