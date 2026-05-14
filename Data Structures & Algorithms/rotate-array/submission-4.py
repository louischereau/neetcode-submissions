class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k = k % n

        while k:
            ptr = nums[0]
            for i in range(n):
                index = (i+1) % n
                temp = nums[index]
                nums[index] = ptr
                ptr = temp
            k -= 1