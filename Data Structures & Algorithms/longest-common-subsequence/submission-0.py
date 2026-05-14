class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        longestSubsequence = 0
        n, m = len(text1), len(text2)
        grid = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    grid[i][j] = 1 + grid[i-1][j-1]
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])
        return grid[n][m]

        