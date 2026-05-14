from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        if len(s1) > len(s2):
            return False

        l, r = 0, n

        while r < len(s2) + 1:
            s1_freq = Counter(s1)
            s2_freq = Counter(s2[l:r])
            if s1_freq == s2_freq: return True
            l+=1
            r+=1

        return False