class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)

        stack = []
        leftmost = [-1] * n

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftmost[i] = stack[-1]
            stack.append(i)

        stack = []
        rightmost = [n] * n

        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightmost[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            l = leftmost[i] + 1
            r = rightmost[i] - 1
            width = r - l + 1
            area = heights[i] * width
            maxArea = max(maxArea, area)

        return maxArea

    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     maxArea = 0
    #     n = len(heights)

    #     for i in range(n):
    
    #         # 1. Expand left as far as possible
    #         l = i
    #         while l >= 0 and heights[l] >= heights[i]:
    #             l -= 1
                
    #         # 2. Expand right as far as possible
    #         r = i
    #         while r < n and heights[r] >= heights[i]:
    #             r += 1

    #         width = r - l - 1
    #         area = heights[i] * width
    #         maxArea = max(maxArea, area)

    #     return maxArea
