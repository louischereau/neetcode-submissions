from collections import defaultdict, Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = defaultdict(list)
        for i, char in enumerate(s):
            if char in hashmap.keys():
            ## Instead of storing list of indeces, better to store first index and count of character
                hashmap[char].append(i)
            else:
                hashmap[char] = [i]
        unique_chars = [indeces[0] for char, indeces in hashmap.items() if len(indeces) == 1]
        if not unique_chars:
            return -1
        return unique_chars[0]

    ## Better performance
    # def firstUniqChar(self, s: str) -> int:
    #     # Counter creates a frequency map: {'l': 1, 'e': 3, ...}
    #     count = Counter(s) 
        
    #     # Manually iterate to find the first index where count is 1
    #     for i, char in enumerate(s):
    #         if count[char] == 1:
    #             return i
        
    #     return -1


        