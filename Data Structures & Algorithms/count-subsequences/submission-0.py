from collections import Counter

class Solution:

    def is_valid_subsequence(self, s: str, t: str, i: int, j: int):
            k = i
            q = 0

            n, m = len(s), len(t)

            while k < j and q < m:
                if s[k] == t[q]:
                    k += 1
                q += 1

            if k == n - 1:
                return True
            
            return False


    def numDistinct(self, s: str, t: str) -> int:

        memo = {}

        n, m = len(s), len(t)

        def dp(i, j):
            
            if j == m:
                return 1

            if i == n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            count = 0

            if s[i] == t[j]:
                count = dp(i+1, j+1) + dp(i + 1, j)
            else:
                count = dp(i + 1, j)

            memo[(i, j)] = count

            return count


        return dp(0, 0)