class Solution:
    def minimumLength(self, s):
        start, end = 0, len(s) - 1
        while start < end and s[start] == s[end]:
            ch = s[end]
            while start <= end and s[end] == ch:
                end -= 1
            while start <= end and s[start] == ch:
                start += 1
        return max(0, end - start + 1)
