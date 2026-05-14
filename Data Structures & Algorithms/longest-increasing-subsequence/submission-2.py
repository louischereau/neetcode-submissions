class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        dp = [1 for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # Update dp[i] if extending the sequence at j is better
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
