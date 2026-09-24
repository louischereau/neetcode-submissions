class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for row in rows:
            for col in range(m):
                matrix[row][col] = 0
        
        for col in cols:
            for row in range(n):
                matrix[row][col] = 0
        
        