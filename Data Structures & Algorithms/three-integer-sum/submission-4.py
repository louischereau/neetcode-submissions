class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return []

        if len(list(set(nums))) == 1 and sum(nums) == 0:
            return [[0,0,0]]

        triplets = []
        nums = sorted(nums)

        for i, num in enumerate(nums):
            pl=i+1
            pr=len(nums) - 1

            while pr > pl:
                result = num + nums[pl] + nums[pr]
                if result == 0:
                    if [num, nums[pl], nums[pr]] not in triplets:
                        triplets.append([num, nums[pl], nums[pr]])
                    pr -= 1
                    pl += 1
                elif result > 0:
                    pr -= 1
                elif result < 0:
                    pl += 1

        return triplets        