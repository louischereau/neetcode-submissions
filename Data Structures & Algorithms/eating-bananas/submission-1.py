import math

class Solution:

    def eatsInTime(self, k: int, piles: List[int], h: int) -> bool:
        return sum(math.ceil(pile / k) for pile in piles) <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low, hi = 1, max(piles)

        while low < hi:
            k = int((hi + low) // 2)
            inTime = self.eatsInTime(k, piles, h)
            if not inTime:
                low = k + 1
            else:
                hi = k
                

        return low


