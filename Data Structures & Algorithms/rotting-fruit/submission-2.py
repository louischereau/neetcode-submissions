
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

    def propagateRot(self, queue: List[List[int]], grid: List[List[int]], freshFruitCount: int) -> int:
        new_queue = []
        for r, c in queue:
            for dr, dc in self.NEIGHBOR_CELLS:
                neighbor_cell = [r + dr, c + dc]
                if self.isCellInGrid(neighbor_cell, len(grid), len(grid[0])):
                    if grid[neighbor_cell[0]][neighbor_cell[1]] == 1:
                        grid[neighbor_cell[0]][neighbor_cell[1]] = 2
                        freshFruitCount -= 1
                        new_queue.append(neighbor_cell)
        queue = new_queue
        return freshFruitCount, queue

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottenFruits = self.findRottenFruits(grid)
        minutes = 0
        queue: List[List[int]] = [rottenFruit for rottenFruit in rottenFruits]
        freshFruitCount = self.countFreshFruits(grid)
        
        while queue and freshFruitCount > 0:
            minutes += 1
            freshFruitCount, queue = self.propagateRot(queue, grid, freshFruitCount)

        if freshFruitCount: minutes = -1

        return minutes
        


        