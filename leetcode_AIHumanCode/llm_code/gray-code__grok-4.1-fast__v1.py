class Solution:
    def grayCode(self, n):
        codes = [0]
        for level in range(n):
            prefix = 1 << level
            size = len(codes)
            pos = size - 1
            while pos >= 0:
                codes.append(prefix | codes[pos])
                pos -= 1
        return codes
