class Solution:
    def reverse(self, x: int) -> int:
        # 1. Define the proper 32-bit boundaries using **
        MIN = -2**31
        MAX = 2**31 - 1
        
        # 2. Track the sign and work entirely with a positive number
        # This completely bypasses Python's tricky negative modulo/division rules!
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        while x:
            digit = x % 10
            res = res * 10 + digit
            x //= 10
        
        # 3. Apply the sign back to the result
        res *= sign
        
        # 4. Do a final bounds check before returning
        if res < MIN or res > MAX:
            return 0
            
        return res