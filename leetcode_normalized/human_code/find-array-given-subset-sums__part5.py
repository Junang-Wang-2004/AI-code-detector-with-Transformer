import collections

class C1(object):

    def recoverArray(self, a1, a2):
        """
        """
        v1 = OrderedDict(sorted(collections.Counter(a2).items()))
        v2 = 0
        v3 = []
        for v4 in range(a1):
            v5 = OrderedDict()
            v6 = iter(v1)
            v7 = next(v6)
            v8 = v7 - next(v6) if v1[v7] == 1 else 0
            assert v8 <= 0
            for v9 in v1.keys():
                if not v1[v9]:
                    continue
                v1[v9 - v8] -= v1[v9] if v8 else v1[v9] // 2
                v5[v9 - v8] = v1[v9]
            v1 = v5
            if v2 in v1:
                v3.append(v8)
            else:
                v3.append(-v8)
                v2 -= v8
        return v3
