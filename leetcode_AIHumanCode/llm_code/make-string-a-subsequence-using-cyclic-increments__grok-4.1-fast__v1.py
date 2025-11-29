class Solution:
    def canMakeSubsequence(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if (ord(t[j]) - ord(s[i])) % 26 <= 1:
                j += 1
            i += 1
        return j == len(t)
