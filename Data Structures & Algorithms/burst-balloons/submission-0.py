class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}

        maxCoins = 0

        n = len(nums)

        nums = [1] + nums + [1]

        def dp(i, j):

            if i > j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            maxCount = 0

            for k in range(i, j + 1):
                maxCount = max(maxCount, dp(i, k - 1) + dp(k+1, j) + nums[i-1] * nums[k] * nums[j+1])


            memo[(i, j)] = maxCount

            return maxCount
            

        return dp(1, n)