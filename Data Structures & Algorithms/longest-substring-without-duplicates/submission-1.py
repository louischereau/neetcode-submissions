class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)

        length, left_ptr, right_ptr = 0, 0, 1

        # unique_char = set(s[left_ptr])

        while right_ptr < len(s):

            print(s[right_ptr], s[left_ptr:right_ptr])
            if s[right_ptr] in s[left_ptr:right_ptr]:
                left_ptr += 1
                if left_ptr == right_ptr: right_ptr += 1
            else:
                # unique_char.add(s[right_ptr])
                right_ptr += 1

            length = max(length, right_ptr - left_ptr)


        return length
        