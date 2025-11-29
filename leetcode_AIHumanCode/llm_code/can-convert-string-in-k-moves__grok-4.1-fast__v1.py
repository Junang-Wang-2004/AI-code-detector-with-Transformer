class Solution:
    def canConvertString(self, s, t, k):
        if len(s) != len(t):
            return False
        freq = [0] * 26
        for i in range(len(s)):
            delta = (ord(t[i]) - ord(s[i])) % 26
            freq[delta] += 1
        for d in range(1, 26):
            m = freq[d]
            if m > 0 and (m - 1) * 26 + d > k:
                return False
        return True
