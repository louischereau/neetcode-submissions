class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_ptr, right_ptr, max_water = 0, len(heights) - 1, 0

        while left_ptr < right_ptr:
            water = (right_ptr - left_ptr) * min(heights[left_ptr], heights[right_ptr])
            max_water = max(max_water, water)
            if heights[left_ptr] < heights[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        return max_water
        