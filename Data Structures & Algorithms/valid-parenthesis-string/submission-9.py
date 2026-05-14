class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_parenthesis = []
        stack_star = []

        for i, char in enumerate(s):
            if char == '(': 
                stack_parenthesis.append(i)
            if char == ')': 
                if stack_parenthesis: 
                    stack_parenthesis.pop()
                else:
                    if stack_star:
                        stack_star.pop()
                    else:
                        return False
            if char == '*': 
                stack_star.append(i)

        while stack_parenthesis and stack_star:
            star_index = stack_star.pop()
            parenth_index = stack_parenthesis[-1]
            if star_index > parenth_index:
                stack_parenthesis.pop()

        return len(stack_parenthesis) == 0 