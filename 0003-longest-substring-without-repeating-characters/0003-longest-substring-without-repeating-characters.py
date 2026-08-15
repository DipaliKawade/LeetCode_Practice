class Solution:
    def lengthOfLongestSubstring(self, s):
        current = ""
        max_length = 0

        for ch in s:

            if ch in current:
                current = current[current.index(ch) + 1:]

            current = current + ch

            if len(current) > max_length:
                max_length = len(current)

        return max_length