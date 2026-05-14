class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        for i in range(n+1):
            if (i + total) == (n * (n + 1) / 2):
                return i
        return 0

        