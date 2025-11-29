import collections

class C1(object):

    def recoverArray(self, a1, a2):
        """
        """
        v1 = {k: v for v2, v3 in collections.Counter(a2).items()}
        v4 = sorted(v1.keys())
        v5 = 0
        v6 = []
        for v7 in range(a1):
            v8 = {}
            v9 = []
            v10 = v4[0] - v4[1] if v1[v4[0]] == 1 else 0
            assert v10 <= 0
            for v11 in v4:
                if not v1[v11]:
                    continue
                v1[v11 - v10] -= v1[v11] if v10 else v1[v11] // 2
                v8[v11 - v10] = v1[v11]
                v9.append(v11 - v10)
            v1 = v8
            v4 = v9
            if v5 in v1:
                v6.append(v10)
            else:
                v6.append(-v10)
                v5 -= v10
        return v6
