import itertools

class C1(object):

    def maxPointsInsideSquare(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = [v1 for v3 in range(26)]
        v4 = v1
        for v5, (v6, v7) in zip(a2, a1):
            v8 = ord(v5) - ord('a')
            v9 = max(abs(v6), abs(v7))
            if v9 < v2[v8]:
                v9, v2[v8] = (v2[v8], v9)
            v4 = min(v4, v9)
        return sum((mn1 < v4 for v10 in v2))
