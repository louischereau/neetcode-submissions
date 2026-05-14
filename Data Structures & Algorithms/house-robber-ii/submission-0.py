class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        def solve(sub_nums):
            memo = {}
            def dp(i):
                if i >= len(sub_nums): return 0
                if i in memo: return memo[i]
                
                res = max(dp(i + 1), sub_nums[i] + dp(i + 2))
                memo[i] = res
                return res
            return dp(0)

        # Case 1: All houses except the last one
        # Case 2: All houses except the first one
        return max(solve(nums[:-1]), solve(nums[1:]))

        