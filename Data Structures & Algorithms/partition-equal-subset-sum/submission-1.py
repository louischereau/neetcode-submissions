class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False
        if len(nums) < 2: return False
        return self.dp(nums, sum(nums)/2)
    
    def dp(self, nums, target):

        if sum(nums) == target: 
            return True

        res = False

        for i in range(len(nums)):
            nums_copy = nums.copy()
            nums_copy.remove(nums[i])
            res = res or self.dp(nums_copy, target)

        return res
        
        