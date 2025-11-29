from collections import deque

class C1(object):

    def findMinHeightTrees(self, a1, a2):
        if not a2:
            return [0] if a1 == 1 else []
        v1 = [[] for v2 in range(a1)]
        v3 = [0] * a1
        for v4, v5 in a2:
            v1[v4].append(v5)
            v1[v5].append(v4)
            v3[v4] += 1
            v3[v5] += 1
        v6 = deque((i for v7 in range(a1) if v3[v7] <= 1))
        v8 = a1
        while v8 > 2:
            v9 = len(v6)
            v8 -= v9
            for v2 in range(v9):
                v10 = v6.popleft()
                for v11 in v1[v10]:
                    v3[v11] -= 1
                    if v3[v11] == 1:
                        v6.append(v11)
        return list(v6)
