class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        memo = {}

        def dp(i, j):
            if i >= n1 and j >= n2:
                return True    

            if (i, j) in memo:
                return memo[(i, j)]

            res = False

            if i < n1 and s1[i] == s3[i+j]:
                res = dp(i+1, j) 
            
            if j < n2 and s2[j] == s3[i+j]:
                res = dp(i, j+1)

            memo[(i, j)] = res

            return res

        return dp(0, 0)