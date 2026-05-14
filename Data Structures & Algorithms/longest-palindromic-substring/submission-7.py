class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n < 2: return s


        dp = [[False for _ in range(n)] for _ in range(n)]

        maxSize = 0

        substring = (0, 0)

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j - i > maxSize:
                        maxSize = j - i
                        substring = (i, j + 1)

        if substring[1] - substring[0] <= 1:
            return s[0]

        return s[substring[0]: substring[1]]