import collections

class C1(object):

    def countPairs(self, a1, a2, a3):
        """
        """
        v1 = [0] * (a1 + 1)
        v2 = collections.Counter(((min(n1, n2), max(n1, n2)) for v3, v4 in a2))
        for v3, v4 in a2:
            v1[v3] += 1
            v1[v4] += 1
        v5 = sorted(v1)
        v6 = []
        for v7, v8 in enumerate(a3):
            v9, v10 = (1, a1)
            v11 = 0
            while v9 < v10:
                if v8 < v5[v9] + v5[v10]:
                    v11 += v10 - v9
                    v10 -= 1
                else:
                    v9 += 1
            for (v12, v13), v14 in v2.items():
                if v1[v12] + v1[v13] - v14 <= v8 < v1[v12] + v1[v13]:
                    v11 -= 1
            v6.append(v11)
        return v6
