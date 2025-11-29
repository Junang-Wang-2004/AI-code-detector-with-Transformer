class C1(object):

    def shareCandies(self, a1, a2):
        v1 = len(a1)
        v2 = {}
        for v3 in range(a2, v1):
            v4 = a1[v3]
            v2[v4] = v2.get(v4, 0) + 1
        v5 = len(v2)
        v6 = a2
        for v7 in range(v1 - a2):
            v8 = a1[v6]
            v2[v8] -= 1
            if v2[v8] == 0:
                del v2[v8]
            v9 = a1[v7]
            if v9 in v2:
                v2[v9] += 1
            else:
                v2[v9] = 1
            v5 = max(v5, len(v2))
            v6 += 1
        return v5
