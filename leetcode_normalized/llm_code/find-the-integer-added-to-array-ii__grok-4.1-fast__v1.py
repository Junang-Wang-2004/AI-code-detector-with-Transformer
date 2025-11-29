import collections

class C1:

    def minimumAddedInteger(self, a1, a2):
        v1 = collections.Counter(a2)
        v2 = max(a2)
        v3 = sorted(a1)
        v4 = v2 - v3[-1]
        v5 = v2 - v3[-2]
        v6 = v2 - v3[-3]
        for v7 in [v4, v5, v6]:
            v8 = collections.Counter((z + v7 for v9 in a1))
            if v1 <= v8:
                return v7
