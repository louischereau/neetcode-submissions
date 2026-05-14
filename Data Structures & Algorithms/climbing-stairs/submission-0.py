class Solution:
    def climbStairs(self, n: int) -> int:
        combinations = [0] * (n+1)
        combinations[0] = 1
        combinations[1] = 1
        for i in range(2, n + 1):
            combinations[i] = combinations[i - 1] + combinations[i - 2]
        return combinations[n]

        