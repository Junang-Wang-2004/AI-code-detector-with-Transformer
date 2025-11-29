class C1(object):

    def stoneGameIII(self, a1):
        """
        """
        v1 = [float('-inf')] * 3
        v1[len(a1) % 3] = 0
        for v2 in reversed(range(len(a1))):
            v3, v4 = (float('-inf'), 0)
            for v5 in range(min(3, len(a1) - v2)):
                v4 += a1[v2 + v5]
                v3 = max(v3, v4 - v1[(v2 + v5 + 1) % 3])
            v1[v2 % 3] = v3
        return ['Tie', 'Alice', 'Bob'][cmp(v1[0], 0)]
