class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        memo = {}

        def dp(index: int) -> int:
            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            if index in memo:
                return memo[index]

            # Path 1: Decode a single digit
            res = dp(index + 1)

            # Path 2: Decode two digits (must be <= 26)
            if index + 1 < len(s):
                if 10 <= int(s[index : index + 2]) <= 26:
                    res += dp(index + 2)

            memo[index] = res
            return res

        return dp(0)
        