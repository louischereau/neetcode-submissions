import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixproduct = [1] * n
        suffixproduct = [1] * n

        for i in range(1, n):
            prefixproduct[i] = nums[i-1] * prefixproduct[i-1]

        for i in range(n - 2, -1, -1):
            suffixproduct[i] = nums[i+1] * suffixproduct[i+1]

        return [suffixproduct[i] * prefixproduct[i] for i in range(n)]