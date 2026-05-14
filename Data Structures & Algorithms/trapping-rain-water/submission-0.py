class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        left_ptr, right_ptr, maxWater = 0, len(height) - 1, 0
        left_max, right_max = height[left_ptr], height[right_ptr]
        
        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
                left_max = max(left_max, height[left_ptr])            
                maxWater += (left_max - height[left_ptr])
            else:
                right_ptr -= 1
                right_max = max(right_max, height[right_ptr])
                maxWater += (right_max - height[right_ptr])
                
        return maxWater

        