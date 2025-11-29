class Solution(object):
    def lastSubstring(self, s):
        n = len(s)
        i = 0
        j = 1
        while j < n:
            k = 0
            while i + k < n and j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k == n or (i + k < n and s[i + k] > s[j + k]):
                j += k + 1
            else:
                i = max(i + k + 1, j)
                j = i + 1
        return s[i:]
