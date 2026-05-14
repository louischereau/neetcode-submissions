class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        lo, hi = 0, M * N - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            val = matrix[mid // N][mid % N]  # convert flat index → 2D
            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False

        