class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= (-1)
        return -1




        