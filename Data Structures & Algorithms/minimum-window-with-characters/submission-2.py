from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        n = len(s)
        n_t = len(t)

        if n < n_t:
            return ""

        t_count = Counter(t)

        if n == n_t and self.checkCounters(Counter(s), t_count):
            return s
        
        if n == n_t and not self.checkCounters(Counter(s), t_count):
            return ""

        l, r = 0, n_t

        minSubstring = None

        while l < r:
            substring = s[l:r]
            if self.checkCounters(Counter(substring), t_count):
                if not minSubstring: minSubstring = substring

                if minSubstring and len(substring) < len(minSubstring):
                    minSubstring = substring
                l += 1
            else:
                if r < n: 
                    r += 1
                else:
                    l += 1


        return minSubstring if minSubstring else ""
            

    def checkCounters(self, count_s, count_t):
        for key, value in count_t.items():
            if key not in count_s or count_t[key] > count_s[key]:
                return False

        return True
        