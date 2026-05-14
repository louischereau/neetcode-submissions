class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return min(nums[0], nums[1])

        if len(nums) == 1:
            return nums[0]

        middle = int(len(nums) / 2)
        
        return min(self.findMin(nums[:middle+1]), self.findMin(nums[middle+1:]))