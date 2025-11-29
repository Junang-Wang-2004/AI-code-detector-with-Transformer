class Solution:
    def isPrefixString(self, s, words):
        pos = 0
        n = len(s)
        for term in words:
            m = len(term)
            if pos + m > n or s[pos:pos + m] != term:
                return False
            pos += m
            if pos == n:
                return True
        return pos == n
