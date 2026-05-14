class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def backtrack(partitionPoint, current):
            if partitionPoint >= len(s):
                result.append(current[:])
                return

            for i in range(partitionPoint, len(s)):
                substring = s[partitionPoint:i+1]
                if substring == substring[::-1]:
                    current.append(substring)
                    backtrack(i+1, current)
                    current.pop()

        backtrack(0, [])
        return result
        