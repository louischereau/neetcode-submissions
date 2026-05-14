class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if hashmap.get(complement) is not None: return [hashmap[complement], i]
            hashmap[num] = i
        return [0, 0]