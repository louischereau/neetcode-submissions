class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        count = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (abs(i - j) < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1


        return count
