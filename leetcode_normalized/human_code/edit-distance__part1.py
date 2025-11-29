class C1(object):

    def minDistance(self, a1, a2):
        if len(a1) < len(a2):
            return self.minDistance(a2, a1)
        v1 = [i for v2 in range(len(a2) + 1)]
        for v2 in range(1, len(a1) + 1):
            v3 = v1[0]
            v1[0] = v2
            for v4 in range(1, len(a2) + 1):
                v5 = v1[v4 - 1] + 1
                v6 = v1[v4] + 1
                v7 = v3
                if a1[v2 - 1] != a2[v4 - 1]:
                    v7 += 1
                v3 = v1[v4]
                v1[v4] = min(v5, v6, v7)
        return v1[-1]
