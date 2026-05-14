class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)

        length, left_ptr, right_ptr = 0, 0, 1

        unique_chars = dict()
        unique_chars[s[left_ptr]] = left_ptr

        while right_ptr < len(s):
            try:
                duplicate_char_position = unique_chars[s[right_ptr]]
                while left_ptr < duplicate_char_position + 1:
                    unique_chars.pop(s[left_ptr])
                    left_ptr += 1
                unique_chars[s[right_ptr]] = right_ptr
                right_ptr += 1
            except:
                unique_chars[s[right_ptr]] = right_ptr
                right_ptr += 1

            length = max(length, right_ptr - left_ptr)
            print(left_ptr, right_ptr)

        return length
        