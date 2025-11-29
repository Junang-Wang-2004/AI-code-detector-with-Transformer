class Solution(object):
    def maxA(self, N):
        if N <= 6:
            return N
        v2, v3, v4, v5, v6 = 2, 3, 4, 5, 6
        for _ in range(N - 6):
            nxt = max(v3 * 3, v2 * 4)
            v2, v3, v4, v5, v6 = v3, v4, v5, v6, nxt
        return v6
