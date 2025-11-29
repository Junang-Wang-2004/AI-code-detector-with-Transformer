class Solution:
    def getSmallestString(self, s):
        n = len(s)
        for pos in range(n - 1):
            left = int(s[pos])
            right = int(s[pos + 1])
            if left % 2 == right % 2 and left > right:
                return s[:pos] + str(right) + str(left) + s[pos + 2:]
        return s
