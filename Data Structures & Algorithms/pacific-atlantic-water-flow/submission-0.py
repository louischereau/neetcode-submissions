class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        HEIGHT, WIDTH = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(border):
            stack = list(border)
            visited = set(border)
            while stack:
                cell = stack.pop()
                for dr, dc in directions:
                    r, c = cell[0] + dr, cell[1] + dc
                    if (0 <= r < HEIGHT and
                        0 <= c < WIDTH and
                        (r, c) not in visited and
                        heights[r][c] >= heights[cell[0]][cell[1]]):
                        visited.add((r, c))
                        stack.append((r, c))
            return visited

        pacific  = [(0, c) for c in range(WIDTH)] + [(r, 0) for r in range(HEIGHT)]
        atlantic = [(HEIGHT-1, c) for c in range(WIDTH)] + [(r, WIDTH-1) for r in range(HEIGHT)]

        return list(dfs(pacific) & dfs(atlantic))