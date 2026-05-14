class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p, s) for p, s in zip(position, speed)]
        
        pair.sort(reverse=True) # car ahead (bigger pos closer to target) first and car behind (smaller pos further from target) after 

        stack = []

        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            # stack[-1] is car behind and stack[-2] is car ahead
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
                 

