class Solution:
    def isDecomposable(self, s):
        pos = 0
        num_twos = 0
        n = len(s)
        while pos < n:
            start = pos
            while pos < n and s[pos] == s[start]:
                pos += 1
            run_len = pos - start
            if run_len not in (2, 3):
                return False
            if run_len == 2:
                num_twos += 1
        return num_twos == 1
