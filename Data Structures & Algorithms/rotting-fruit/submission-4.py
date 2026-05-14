
class Solution:

    NEIGHBOR_CELLS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def countFreshFruits(self, grid: List[List[int]]) -> int:
        freshFruitCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    freshFruitCount += 1
        return freshFruitCount

    def findRottenFruits(self, grid: List[List[int]]) -> int:
        rottenFruits: List[List[int]] = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rottenFruits.append([row, col])
        return rottenFruits

    def isCellInGrid(self, cell: List[int], rows: int, columns: int) -> bool:
        return 0 <= cell[0] <= rows - 1 and 0 <= cell[1] <= columns - 1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = self.findRottenFruits(grid)
        minutes = 0
        freshFruitCount = self.countFreshFruits(grid)
        
        if freshFruitCount == 0: return minutes
        
        while queue and freshFruitCount > 0:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.pop(0)
                for dr, dc in self.NEIGHBOR_CELLS:
                    neighbor_cell = [r + dr, c + dc]
                    if self.isCellInGrid(neighbor_cell, len(grid), len(grid[0])):
                        if grid[neighbor_cell[0]][neighbor_cell[1]] == 1:
                            grid[neighbor_cell[0]][neighbor_cell[1]] = 2
                            freshFruitCount -= 1
                            queue.append(neighbor_cell)

        return minutes if not freshFruitCount else -1
        


        