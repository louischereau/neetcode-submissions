class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        LSB = digits[-1]
        n = len(digits)

        # if LSB < 9:
        #     LSB += 1
        #     digits[-1] = LSB
        # else:
        #     digits[-1] = 0
        for i in range(n - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            else:
                digits[i] += 1
                break
        
        return digits

        