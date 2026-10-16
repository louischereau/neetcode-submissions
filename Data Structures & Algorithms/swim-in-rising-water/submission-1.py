import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)

        start_r, start_c = 0, 0
        end_r, end_c = n -1, n - 1

        heap = [(grid[start_r][start_c], start_r, start_c)]

        visited = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:

            h, row, col = heapq.heappop(heap)

            if row == end_r and col == end_c:
                return h

            if (row, col) in visited:
                continue
            
            visited.add((row, col))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < n:
                    heapq.heappush(heap, (max(grid[nr][nc], h), nr, nc))
        
        return -1






        