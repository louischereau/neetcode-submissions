import math 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = []
        def solve(x: int, y: int, path: List[int]) -> None:
            
            if x == m - 1 and y == n - 1:
                paths.append(path)
                return

            path.append([x, y])

            if x == m - 1:
                solve(x, y+1, path)
            elif y == n - 1: 
                solve(x+1, y, path) 
            else:
                solve(x+1, y, path)
                solve(x, y + 1, path)


        solve(0, 0, [])

        return len(paths)