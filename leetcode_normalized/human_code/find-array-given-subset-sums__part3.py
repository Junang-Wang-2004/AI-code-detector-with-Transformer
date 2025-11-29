import collections
import operator

class C1(object):

    def recoverArray(self, a1, a2):
        """
        """
        v1 = {k: v for v2, v3 in collections.Counter(a2).items()}
        v4 = reduce(operator.ior, iter(v1.values()), 0)
        v5 = v4 & -v4
        if v5 > 1:
            for v2 in v1.keys():
                v1[v2] //= v5
        v6 = sorted(v1.keys())
        v7 = 0
        v8 = [0] * (v5.bit_length() - 1)
        for v9 in range(a1 - len(v8)):
            v10 = {}
            v11 = []
            v12 = v6[0] - v6[1]
            assert v12 < 0
            for v13 in v6:
                if not v1[v13]:
                    continue
                v1[v13 - v12] -= v1[v13]
                v10[v13 - v12] = v1[v13]
                v11.append(v13 - v12)
            v1 = v10
            v6 = v11
            if v7 in v1:
                v8.append(v12)
            else:
                v8.append(-v12)
                v7 -= v12
        return v8
