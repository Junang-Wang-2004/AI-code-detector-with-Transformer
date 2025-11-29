import itertools
from functools import reduce

class C1(object):

    def minimumCost(self, a1, a2, a3):
        """
        """
        v1 = float('inf')
        v2 = max((len(w) for v3 in a2))
        v4 = [v1] * (v2 + 1)
        v4[0] = 0
        for v5 in range(len(a1)):
            if v4[v5 % len(v4)] == v1:
                continue
            for v3, v6 in zip(a2, a3):
                if a1[v5:v5 + len(v3)] == v3:
                    v4[(v5 + len(v3)) % len(v4)] = min(v4[(v5 + len(v3)) % len(v4)], v4[v5 % len(v4)] + v6)
            v4[v5 % len(v4)] = v1
        return v4[len(a1) % len(v4)] if v4[len(a1) % len(v4)] != v1 else -1
