class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k
        n = len(nums)
        res = []

        while r < n + 1:
            window = nums[l:r]
            window.sort()
            maxNum = window[-1]
            res.append(maxNum)
            r += 1
            l += 1
        
        return res


        