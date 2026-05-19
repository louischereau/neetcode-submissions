class Solution:
    def isHappy(self, n: int) -> bool:
        viewed = set()
        while n != 1:
            res = 0
            for digit in str(n):
                res += pow(int(digit), 2)
            if res in viewed:
                return False
            else:
                viewed.add(res)
            n = res
        
        return True
