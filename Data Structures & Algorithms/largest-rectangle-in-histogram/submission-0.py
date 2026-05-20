class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)

        for i in range(n):
    
            # 1. Expand left as far as possible
            l = i
            while l >= 0 and heights[l] >= heights[i]:
                l -= 1
                
            # 2. Expand right as far as possible
            r = i
            while r < n and heights[r] >= heights[i]:
                r += 1

            width = r - l - 1
            area = heights[i] * width
            maxArea = max(maxArea, area)

        return maxArea
