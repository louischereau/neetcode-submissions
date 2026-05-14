class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False
        if len(nums) < 2: return False
        memo = {}

        def dp(index, target):

            if target == 0: 
                return True

            if index > len(nums) - 1:
                return False

            state = (index, target)

            if state in memo:
                return memo[state]

            # Decision 1: Use the current number
            # Decision 2: Skip the current number
            result = dp(index+1, target - nums[index]) or dp(index+1, target)

            memo[state] = result

            return result
        

        return dp(0, sum(nums)/2)
    
    
        