import collections
from functools import reduce

class C1(object):

    def recoverArray(self, a1, a2):
        """
        """
        v1, v2 = (min(a2), max(a2))
        v3 = [0] * (v2 - v1 + 1)
        for v4 in a2:
            v3[v4 - v1] += 1
        v5 = [v4 for v4 in range(v1, v2 + 1) if v3[v4 - v1]]
        v6 = 0
        v7 = []
        for v8 in range(a1):
            v9 = [0] * (v2 - v1 + 1)
            v10 = []
            v11 = v5[0] - v5[1] if v3[v5[0] - v1] == 1 else 0
            assert v11 <= 0
            for v4 in v5:
                if not v3[v4 - v1]:
                    continue
                v3[v4 - v11 - v1] -= v3[v4 - v1] if v11 else v3[v4 - v1] // 2
                v9[v4 - v11 - v1] = v3[v4 - v1]
                v10.append(v4 - v11)
            v3 = v9
            v5 = v10
            if v3[v6 - v1]:
                v7.append(v11)
            else:
                v7.append(-v11)
                v6 -= v11
        return v7
