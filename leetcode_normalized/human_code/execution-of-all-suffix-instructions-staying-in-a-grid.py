import collections

class C1(object):

    def executeInstructions(self, a1, a2, a3):
        """
        """
        v1 = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
        (v2, v3), (v4, v5) = (a2, (0, 0))
        v6 = list(range(len(a3), 0, -1))
        v7 = collections.defaultdict(list)
        v8 = collections.defaultdict(list)
        v7[v2 - v4].append(0)
        v8[v3 - v5].append(0)
        for v9, v10 in enumerate(a3):
            v11, v12 = v1[v10]
            v4, v5 = (v4 + v11, v5 + v12)
            for v13 in (a1 - v4, -v4 - 1):
                if v13 not in v7:
                    continue
                for v14 in v7[v13]:
                    v6[v14] = min(v6[v14], v9 - v14)
                v7[v13] = []
            for v13 in (a1 - v5, -v5 - 1):
                if v13 not in v8:
                    continue
                for v14 in v8[v13]:
                    v6[v14] = min(v6[v14], v9 - v14)
                v8[v13] = []
            v7[v2 - v4].append(v9 + 1)
            v8[v3 - v5].append(v9 + 1)
        return v6
