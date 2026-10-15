class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        n, m = len(s), len(p)

        def dp(i, j):

            if j == m and i == n:
                return True

            if i >= n:
                while j + 1 < m and p[j + 1] == '*':
                    j += 2
                return j == m

            if j >= m:
                return False

            
            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] != p[j] and p[j] != '.' and j < m - 1 and p[j + 1] != '*':
                return False

            if j < m - 1 and p[j + 1] == '*':
                if s[i] == p[j] or p[j] == '.':
                    res = dp(i + 1, j) or dp(i, j+2)
                else:
                    res = dp(i, j+2)
                memo[(i, j)] = res
                return res


            
            if s[i] == p[j] or p[j] == '.':
                res = dp(i+1, j+1)
                memo[(i, j)] = res
                return res

            
            
            return False


        
        return dp(0, 0)
        