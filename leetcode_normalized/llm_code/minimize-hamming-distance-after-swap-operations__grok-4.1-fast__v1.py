import collections
from collections import deque

class C1:

    def minimumHammingDistance(self, a1, a2, a3):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a3:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = [False] * v1
        v7 = 0
        for v8 in range(v1):
            if v6[v8]:
                continue
            v9 = []
            v10 = deque([v8])
            v6[v8] = True
            while v10:
                v11 = v10.popleft()
                v9.append(v11)
                for v12 in v2[v11]:
                    if not v6[v12]:
                        v6[v12] = True
                        v10.append(v12)
            v13 = collections.Counter((a1[i] for v14 in v9))
            v15 = collections.Counter((a2[v14] for v14 in v9))
            v16 = v13 - v15
            v7 += sum(v16.values())
        return v7
