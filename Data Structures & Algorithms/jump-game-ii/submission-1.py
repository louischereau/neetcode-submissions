class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        current_furthest = 0
        min_jumps = 0

        if len(nums) <= 1:
            return 0

        for i in range(len(nums)):
            furthest = max(furthest, i + nums[i])
            if i == current_furthest:
                min_jumps += 1
                current_furthest = furthest
                # Optimization: If the new range already hits the end, we can stop.
                if current_furthest >= len(nums) - 1:
                    break


        return min_jumps