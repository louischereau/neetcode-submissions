class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        current = nums[0]
        startFrom = 0

        for i in range(1, len(nums)):
            subarraySum = sum(nums[startFrom:i+1])
            if subarraySum < 0: startFrom = i + 1
            current = max(current + nums[i], nums[i])
            maxSum = max(maxSum, current)

        return maxSum
