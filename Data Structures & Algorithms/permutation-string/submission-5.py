from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        l, r = 0, n1

        if n1 > n2:
            return False

        while r < n2 + 1:
            s1_freq = Counter(s1)
            s2_freq = Counter(s2[l:r])
            if s1_freq == s2_freq: return True
            l+=1
            r+=1

        return False