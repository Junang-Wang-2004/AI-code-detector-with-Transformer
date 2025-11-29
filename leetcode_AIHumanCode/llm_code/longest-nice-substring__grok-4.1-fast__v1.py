class Solution:
    def longestNiceSubstring(self, s):
        n = len(s)
        result = ""
        max_len = 0
        for i in range(n):
            low_mask = 0
            up_mask = 0
            for j in range(i, n):
                ch = s[j].lower()
                shift = ord(ch) - ord('a')
                b = 1 << shift
                if s[j].islower():
                    low_mask |= b
                else:
                    up_mask |= b
                curr_len = j - i + 1
                if low_mask == up_mask and curr_len > max_len:
                    max_len = curr_len
                    result = s[i:j+1]
        return result
