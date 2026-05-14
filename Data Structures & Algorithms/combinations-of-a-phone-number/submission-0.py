class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        MAPPING = {
            1: [],
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"], 
        }

        def backtrack(start, current):
            if len(current) == len(digits):
                result.append(current[:])
                return
            
            for c in MAPPING[int(digits[start])]:
                backtrack(start + 1, current + c)

        if digits:
            backtrack(0, "")

        return result