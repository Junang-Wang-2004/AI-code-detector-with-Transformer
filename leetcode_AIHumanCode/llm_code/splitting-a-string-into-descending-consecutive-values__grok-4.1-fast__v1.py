class Solution(object):
    def splitString(self, s):
        n = len(s)
        def helper(pos, val):
            if val < 0:
                return False
            t = str(val)
            m = len(t)
            if pos + m > n or s[pos:pos + m] != t:
                return False
            next_pos = pos + m
            if next_pos == n:
                return True
            return helper(next_pos, val - 1)
        for length in range(1, n):
            if s[0] == '0' and length > 1:
                continue
            prev = int(s[:length])
            if helper(length, prev - 1):
                return True
        return False
