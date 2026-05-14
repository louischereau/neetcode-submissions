class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        if n == 0: return 0
        memo = {}

        def dp(index, acc):
            if acc > amount or index >= n:
                return 0

            if (index, acc) in memo:
                return memo[(index, acc)]

            if acc == amount:
                return 1

            res = dp(index, acc+coins[index]) + dp(index+1, acc)

            memo[(index, acc)] = res

            return res

        return dp(0, 0)