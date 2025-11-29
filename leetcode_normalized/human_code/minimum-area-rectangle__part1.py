import collections

class C1(object):

    def minAreaRect(self, a1):
        """
        """
        v1 = len(set((x for v2, v3 in a1)))
        v4 = len(set((v3 for v2, v3 in a1)))
        v5 = collections.defaultdict(list)
        if v1 > v4:
            for v2, v3 in a1:
                v5[v2].append(v3)
        else:
            for v2, v3 in a1:
                v5[v3].append(v2)
        v6 = {}
        v7 = float('inf')
        for v2 in sorted(v5):
            v5[v2].sort()
            for v8 in range(len(v5[v2])):
                for v9 in range(v8):
                    v10, v11 = (v5[v2][v9], v5[v2][v8])
                    if (v10, v11) in v6:
                        v7 = min(v7, (v2 - v6[v10, v11]) * (v11 - v10))
                    v6[v10, v11] = v2
        return v7 if v7 != float('inf') else 0
