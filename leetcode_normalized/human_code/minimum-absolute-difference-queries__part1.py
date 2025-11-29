class C1(object):

    def minDifference(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = [[0] * (max(a1) + 1)]
        for v3 in a1:
            v2.append(v2[-1][:])
            v2[-1][v3] += 1
        v4 = []
        for v5, v6 in a2:
            v7, v8 = (v1, -1)
            for v3 in range(len(v2[0])):
                if not v2[v5][v3] < v2[v6 + 1][v3]:
                    continue
                if v8 != -1:
                    v7 = min(v7, v3 - v8)
                v8 = v3
            v4.append(v7 if v7 != v1 else -1)
        return v4
