import collections
import itertools
from collections import defaultdict

class C1:

    def generateSentences(self, a1, a2):
        v1 = set()
        for v2 in a1:
            v1.update(v2)
        v3 = defaultdict(list)
        for v4, v5 in a1:
            v3[v4].append(v5)
            v3[v5].append(v4)
        v6 = set()
        v7 = {}

        def dfs(a1, a2):
            a2.append(a1)
            v6.add(a1)
            for v1 in v3[a1]:
                if v1 not in v6:
                    dfs(v1, a2)
        for v8 in sorted(v1):
            if v8 not in v6:
                v9 = []
                dfs(v8, v9)
                v10 = sorted(v9)
                for v11 in v10:
                    v7[v11] = v10
        v12 = a2.split()
        v13 = []
        for v8 in v12:
            if v8 not in v7:
                v13.append([v8])
            else:
                v13.append(v7[v8])
        return [' '.join(combo) for v14 in itertools.product(*v13)]
