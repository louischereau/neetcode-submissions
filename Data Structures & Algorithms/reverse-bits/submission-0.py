class Solution:
    def reverseBits(self, n: int) -> int:
        binary = format(n, 'b')
        while len(binary) < 32:
            binary = '0' + binary
        binary = binary[::-1]
        return int(binary, 2)
        

        