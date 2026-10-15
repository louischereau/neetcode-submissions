class Solution:

    

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        n, m = len(matrix), len(matrix[0])

        memo = {}

        visited = set()

        longestPath = 0

        UP = (-1, 0)
        DOWN = (1, 0)
        LEFT = (0, -1)
        RIGHT = (0, 1)

        directions = [UP, DOWN, LEFT, RIGHT]

        def dfs(i, j):
 
            if memo.get((i, j)):
                return memo[(i, j)]

            maxPath = 1

            for dr, dc in directions:
                row, col = i + dr, j + dc
                if 0 <= row < n and 0 <= col < m and (row, col) not in visited and matrix[row][col] > matrix[i][j]:
                    maxPath = max(maxPath, 1 + dfs(row, col))
            
            memo[(i, j)] = maxPath

            return maxPath
        
        # Check every cell as potential startign point 
        global_max = 0
        for r in range(n):
            for c in range(m):
                global_max = max(global_max, dfs(r, c))
        

        return global_max