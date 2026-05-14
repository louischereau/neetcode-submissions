class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0: return 0

        memo = {}

        def dp(index):
            if index >= n:
                return 0

            if index in memo:
                return memo[index]

            result = max(dp(index+1), nums[index] + dp(index+2))

            memo[index] = result

            return result

        return dp(0)
