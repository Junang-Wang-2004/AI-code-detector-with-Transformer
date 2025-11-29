class Solution(object):
    def isOneEditDistance(self, s, t):
        ls, lt = len(s), len(t)
        if abs(ls - lt) > 1:
            return False
        i, j = 0, 0
        while i < ls and j < lt:
            if s[i] != t[j]:
                if ls == lt:
                    return s[i + 1:] == t[j + 1:]
                return s[i:] == t[j + 1:] if ls < lt else s[i + 1:] == t[j:]
            i += 1
            j += 1
        return abs(ls - lt) == 1
