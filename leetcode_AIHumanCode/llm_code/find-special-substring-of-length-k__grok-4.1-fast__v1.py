class Solution(object):
    def hasSpecialSubstring(self, s, k):
        idx = 0
        slen = len(s)
        while idx < slen:
            end = idx + 1
            while end < slen and s[end] == s[idx]:
                end += 1
            if end - idx == k:
                return True
            idx = end
        return False
