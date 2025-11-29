from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        if not matrix or not matrix[0]:
            return 0
        r, c = len(matrix), len(matrix[0])
        res = float('-inf')
        if r > c:
            matrix = [list(t) for t in zip(*matrix)]
            r, c = c, r
        for top in range(r):
            temp = [0] * c
            for bot in range(top, r):
                for j in range(c):
                    temp[j] += matrix[bot][j]
                prefixes = [0]
                pref = 0
                for x in temp:
                    pref += x
                    idx = bisect_left(prefixes, pref - k)
                    if idx < len(prefixes):
                        res = max(res, pref - prefixes[idx])
                    insort(prefixes, pref)
        return res
