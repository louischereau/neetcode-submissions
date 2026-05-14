class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(current, used):
            if len(current) == len(nums):
                results.append(current[:])
                return

            for i in range(len(nums)):
                if used[i]: continue
                current.append(nums[i])
                used[i] = True
                backtrack(current, used)
                used[i] = False
                current.pop()

        backtrack([], [False] * len(nums))
        return results