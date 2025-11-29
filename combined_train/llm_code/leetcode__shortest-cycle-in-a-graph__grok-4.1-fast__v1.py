from collections import deque
from math import inf

class C1:

    def findShortestCycle(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = inf
        for v6 in range(a1):
            v7 = [-1] * a1
            v7[v6] = 0
            v8 = [-1] * a1
            v9 = deque([v6])
            while v9:
                v10 = v9.popleft()
                if 2 * v7[v10] + 1 >= v5:
                    break
                for v11 in v1[v10]:
                    if v7[v11] == -1:
                        v7[v11] = v7[v10] + 1
                        v8[v11] = v10
                        if 2 * v7[v11] + 1 >= v5:
                            continue
                        v9.append(v11)
                    elif v11 != v8[v10]:
                        v12 = v7[v10] + v7[v11] + 1
                        if v12 < v5:
                            v5 = v12
        return int(v5) if v5 != inf else -1
