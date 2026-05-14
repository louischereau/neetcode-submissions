class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n > 0:
            for _ in range(n):
                res *= x
        elif n < 0:
            for _ in range(abs(n)):
                res *= 1/x
        else:
            res = 1
        return res
        