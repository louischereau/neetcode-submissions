class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        maxLength, l, r = 0, 0 ,0
        char_count = { key: 0 for key in [chr(x) for x in range(ord('A'), ord('Z')+1)] }

        while r < len(s):
            char_count[s[r]] += 1
            mostFrequentCharCount = max(char_count.values())
            if r - l + 1 - mostFrequentCharCount <= k:
                maxLength = max(maxLength, r - l + 1)
                r += 1
            else:
                char_count[s[l]] -= 1
                l += 1
                r += 1

        return maxLength
        
        