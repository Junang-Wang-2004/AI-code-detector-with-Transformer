class C1(object):

    def findPrimePairs(self, a1):
        if a1 < 4:
            return []
        v1 = [True] * (a1 + 1)
        v1[0] = v1[1] = False
        for v2 in range(2, int(a1 ** 0.5) + 1):
            if v1[v2]:
                for v3 in range(v2 * v2, a1 + 1, v2):
                    v1[v3] = False
        v4 = []
        for v2 in range(2, a1 // 2 + 1):
            if v1[v2] and v1[a1 - v2]:
                v4.append([v2, a1 - v2])
        return v4
