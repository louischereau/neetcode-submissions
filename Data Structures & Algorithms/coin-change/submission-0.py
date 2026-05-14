class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if not amount: return 0

        maxValue = amount + 1

        fewestNumberOfCoins = [maxValue] * (amount+1)

        fewestNumberOfCoins[0] = 0
        
        for i in range(1, amount+1): 
            for coin in coins:
                if i - coin >= 0:
                    fewestNumberOfCoins[i] = min(fewestNumberOfCoins[i], 1 + fewestNumberOfCoins[i - coin])
        
        return fewestNumberOfCoins[amount] if fewestNumberOfCoins[amount] != maxValue else -1

        