from collections import deque

class Solution:

    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def bfs(self, grid: List[List[int]], start_row: int, start_col: int) -> int:
        queue = deque([[start_row, start_col]])
        area = 1
        GRID_HEIGHT, GRID_WIDTH = len(grid), len(grid[0])
        grid[start_row][start_col] = -1

        while queue:
            row, col = queue.popleft()

            for direction in self.DIRECTIONS:
                drow, dcol = direction
                next_row, next_col = row + drow, col + dcol
                if 0 <= next_row < GRID_HEIGHT and 0 <= next_col < GRID_WIDTH and grid[next_row][next_col] == 1:
                    grid[next_row][next_col] = -1
                    queue.append([next_row, next_col])
                    area += 1

        return area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        GRID_HEIGHT, GRID_WIDTH = len(grid), len(grid[0])
        islandAreas=[]

        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if grid[row][col] == 1:
                    islandArea = self.bfs(grid, row, col)
                    islandAreas.append(islandArea)

        if not islandAreas:
            return 0

        return max(islandAreas)
        