class Solution:

    def findNeighboringLand(self, position: Tuple[int, int], grid: List[List[str]]) ->  List[List[str]]:
        stack = [position]

        while stack:
            cell = stack.pop()
            grid[cell[0]][cell[1]] = 'X'
            
            top = (max(cell[0] - 1, 0), cell[1])
            bottom = (min(cell[0] + 1, len(grid) - 1), cell[1])
            left = (cell[0], max(cell[1] - 1, 0))
            right = (cell[0], min(cell[1] + 1, len(grid[0]) - 1))

            countours = (top, bottom, left, right)

            for neighbor in countours:
                if grid[neighbor[0]][neighbor[1]] == '1':
                    stack.append(neighbor)

        return grid


    def numIslands(self, grid: List[List[str]]) -> int:

        numIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid = self.findNeighboringLand((i, j), grid)
                    numIslands += 1

        return numIslands




