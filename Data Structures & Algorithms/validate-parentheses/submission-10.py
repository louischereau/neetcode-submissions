class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) > 1 and abs(ord(stack[-1]) - ord(stack[-2])) <= 2 and ord(stack[-1]) != ord(stack[-2]) and ord(stack[-2]) < ord(stack[-1]):
                stack.pop()
                stack.pop()
            else:
                continue
        return len(stack) == 0
        