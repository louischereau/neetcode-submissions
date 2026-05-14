class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        ptr = 0

        if t in s: return 0

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[ptr]
            if char_s == char_t: ptr += 1

        return len(t) - ptr

        