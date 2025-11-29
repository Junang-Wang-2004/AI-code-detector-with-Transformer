class Solution(object):
    def minOperations(self, s, k):
        n = len(s)
        zeros = sum(c == '0' for c in s)
        ones = n - zeros
        for ops in range(n + 1):
            flips = ops * k
            if flips < zeros or (flips - zeros) % 2 != 0:
                continue
            if ops % 2 == 0:
                upper = zeros * (ops - 1) + ones * ops
            else:
                upper = zeros * ops + ones * (ops - 1)
            if flips <= upper:
                return ops
        return -1
