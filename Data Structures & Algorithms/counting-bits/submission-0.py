class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for number in range(n + 1):
            result.append(int(bin(number).count('1')))
        return result
        