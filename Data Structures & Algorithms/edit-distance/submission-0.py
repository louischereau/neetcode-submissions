class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        memo = {}

        def dp(i, j):

            if i >= n1 and j < n2:
                return n2 - j

            if j >= n2 and i < n1:
                return n1 - i

            if i >= n1 and j >= n2:
                return 0 

            if (i, j) in memo:
                return memo[(i, j)]

            res = 0
            
            # Insert: You stay at i in word1 but move forward to j+1 in word2.

            # Delete: You move forward to i+1 in word1 but stay at j in word2.

            # Replace: You move forward in both (i+1, j+1)

            if word1[i] != word2[j]:
                res = 1 + min(dp(i+1, j), dp(i, j+1), dp(i+1, j+1))
            else:
                res = dp(i+1, j+1)

            memo[(i, j)] = res

            return res

        return dp(0, 0)
        