from collections import deque

class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = deque([])

        du = (-1, 0)
        dd = (1, 0)
        dl = (0, -1)
        dr = (0, 1)

        HEIGHT, WIDTH = len(grid) - 1, len(grid[0]) - 1

        visited = set()

        distance = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:

            for _ in range(len(queue)):
                
                cell = queue.popleft()

                for direction in [du, dd, dl, dr]:
                    row = cell[0] + direction[0]
                    col = cell[1] + direction[1]
                    if 0 <= row <= HEIGHT and 0 <= col <= WIDTH:
                        if tuple((row, col)) not in visited:
                            if grid[row][col] == 2147483647:
                                grid[row][col] = distance + 1
                                queue.append((row, col))
                                visited.add((row, col))

            distance += 1
                
