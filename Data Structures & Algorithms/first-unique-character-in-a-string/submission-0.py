from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = defaultdict(list)
        for i, char in enumerate(s):
            if char in hashmap.keys():
                hashmap[char].append(i)
            else:
                hashmap[char] = [i]
        unique_chars = [indeces[0] for char, indeces in hashmap.items() if len(indeces) == 1]

        if not unique_chars:
            return -1
        return unique_chars[0]


        