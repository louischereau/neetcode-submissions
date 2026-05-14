import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        inverted_stones = [-1 * x for x in stones]
        heapq.heapify(inverted_stones)

        while len(inverted_stones) > 1:
            stone1 = heapq.heappop(inverted_stones)
            stone2 = heapq.heappop(inverted_stones)
            diff = abs(abs(stone1) - abs(stone2))
            if diff > 0:
                heapq.heappush(inverted_stones, -1 * diff)
            
        
        return abs(inverted_stones[0]) if len(inverted_stones) == 1 else 0