class Solution:
    def decodeCiphertext(self, s, r):
        n = len(s)
        if r == 0:
            return ""
        w = n // r
        res = []
        stride = w + 1
        for start in range(w):
            pos = start
            while pos < n:
                res.append(s[pos])
                pos += stride
        while res and res[-1] == ' ':
            res.pop()
        return ''.join(res)
