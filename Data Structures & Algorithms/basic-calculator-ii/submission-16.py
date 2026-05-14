from enum import Enum

class Operator(Enum):
    M = '*'
    D = '/'
    A = '+'
    S = '-'

class Solution:
    
    def isCharNumber(self, char: str) -> bool:
        return 0 <= ord(char) - ord('0') <= 9 

    def isCharOperator(self, char: str) -> bool:
        return char in [Operator.A.value, Operator.S.value, Operator.M.value, Operator.D.value]

    def retrieveMultiDigitNumber(self, s: str, start_index: int) -> Tuple[str, int]:
        number = s[start_index] + s[start_index+1]

        i = start_index + 2

        while i < len(s) and self.isCharNumber(s[i]):
            number += s[i]
            i += 1

        return (number, i - 1)

    def addToStack(self, stack: List[int], number: str, currentOperation: str) -> None:
        if currentOperation == Operator.A.value:
            stack.append(int(number))
        elif currentOperation == Operator.S.value:
            stack.append(-1 * int(number))
        elif currentOperation == Operator.M.value:
            lastNumber = stack.pop()
            newNumber = lastNumber * int(number)
            stack.append(newNumber)
        elif currentOperation == Operator.D.value:
            lastNumber = stack.pop()
            newNumber = int(lastNumber / int(number))
            stack.append(newNumber)
        else:
            return



    def calculate(self, s: str) -> int:
        currentOperation = Operator.A.value
        stack = []

        s = s.strip()

        i = 0

        while i < len(s):
            if self.isCharOperator(s[i]):
                currentOperation = s[i]
            elif self.isCharNumber(s[i]):
                if i + 1 < len(s) and not self.isCharNumber(s[i+1]):
                    self.addToStack(stack, s[i], currentOperation)
                    # stack.append(int(s[i]))
                elif i + 1 < len(s) and self.isCharNumber(s[i+1]):
                    multiDigitNumber, j = self.retrieveMultiDigitNumber(s, i)
                    self.addToStack(stack, multiDigitNumber, currentOperation)
                    # stack.append(int(multiDigitNumber))
                    i = j
                elif i + 1 == len(s) and self.isCharNumber(s[i]):
                    self.addToStack(stack, s[i], currentOperation)

            i += 1


        return sum(stack)






        