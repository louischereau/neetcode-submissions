class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        res = [0] * (n+m)

        if num1 == "0" or num2 == "0":
            return "0"

        for i in range(n-1, -1, -1):
            for j in range(m-1 , -1, -1):
                mul = (ord(num2[j]) - ord('0')) * (ord(num1[i]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                total = res[p2] + mul
                res[p2] = total % 10
                res[p1] += total // 10
        
        start = 0 if res[0] != 0 else 1
        
        return "".join(map(str, res[start:]))




            




