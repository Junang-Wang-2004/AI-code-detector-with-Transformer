class C1(object):

    def cheapestJump(self, a1, a2):
        """
        """
        v1 = []
        if not a1 or a1[-1] == -1:
            return v1
        v2 = len(a1)
        v3, v4 = ([float('inf')] * v2, [-1] * v2)
        v3[v2 - 1] = a1[v2 - 1]
        for v5 in reversed(range(v2 - 1)):
            if a1[v5] == -1:
                continue
            for v6 in range(v5 + 1, min(v5 + a2 + 1, v2)):
                if a1[v5] + v3[v6] < v3[v5]:
                    v3[v5] = a1[v5] + v3[v6]
                    v4[v5] = v6
        if v3[0] == float('inf'):
            return v1
        v7 = 0
        while v7 != -1:
            v1.append(v7 + 1)
            v7 = v4[v7]
        return v1
