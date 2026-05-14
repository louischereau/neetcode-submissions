class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
                            
        memo = {}

        def dp(index, buying=True):
            if index >= n: return 0
            if (index, buying) in memo: return memo[(index, buying)]
            res = 0
            if buying:
                res = max(-prices[index] + dp(index+1, False), dp(index+1, True))
            else:
                res = max(prices[index] + dp(index+2, True), dp(index+1, False))

            memo[(index, buying)] = res
            return res


        return dp(0)