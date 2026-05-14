class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left_ptr, right_ptr = 0, 1

        while right_ptr < len(prices):
            maxP = max(maxP, prices[right_ptr] - prices[left_ptr])
            if prices[right_ptr] < prices[left_ptr]: 
                left_ptr += 1
            else: right_ptr += 1

        return maxP

        