class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = format(n, 'b')
        return sum([int(bit) for bit in bits])

        