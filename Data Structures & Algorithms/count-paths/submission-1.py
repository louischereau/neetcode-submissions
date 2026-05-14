import math 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]

        def solve(x: int, y: int) -> int:

            if x == m - 1 and y == n - 1:
                return 1

            if memo[x][y] != -1:
                return memo[x][y]

            if x == m - 1:
                return solve(x, y+1)
            
            if y == n - 1:
                return solve(x+1, y)
            
            memo[x][y] = solve(x+1,y) + solve(x, y+1)

            return memo[x][y]

        return solve(0, 0)