class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0: return 0
        memo = {}

        def dp(index, acc):

            if index == n:
                if acc == target:
                    return 1
                else:
                    return 0

            if (index, acc) in memo:
                return memo[(index, acc)]

            res = dp(index+1, acc + nums[index]) + dp(index+1, acc - nums[index])

            memo[(index, acc)] = res

            return res
 

        return dp(0, 0)