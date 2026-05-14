from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        substringSizes = []
        substring = []
        for letter in s:
            count[letter] -= 1
            substring.append(letter)
            if self.endSubstring(count, substring):
                substringSizes.append(len(substring))
                substring = []


        return substringSizes

    def endSubstring(self, count, substring):
        total = 0

        for letter in set(substring):
            total += count[letter]

        return total == 0

        