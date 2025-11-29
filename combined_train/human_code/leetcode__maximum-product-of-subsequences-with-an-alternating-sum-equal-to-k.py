import collections

class C1(object):

    def maxProduct(self, a1, a2, a3):
        """
        """
        v1 = sum(a1)
        if a2 > v1 or a2 < -v1:
            return -1
        v2 = collections.defaultdict(set)
        for v3 in a1:
            v4 = collections.defaultdict(set, {a2: set(v) for a2, v5 in v2.items()})
            v4[1, v3].add(min(v3, a3 + 1))
            for (v6, v1), v7 in v2.items():
                v8 = (v6 ^ 1, v1 + (v3 if v6 == 0 else -v3))
                for v5 in v7:
                    v4[v8].add(min(v5 * v3, a3 + 1))
            v2 = v4
        v9 = -1
        for (v6, v1), v7 in v2.items():
            if v1 != a2:
                continue
            for v5 in v7:
                if v5 <= a3:
                    v9 = max(v9, v5)
        return v9
