from collections import deque

class C1:

    def minReorder(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        v3 = set()
        for v4, v5 in a2:
            v1[v4].append(v5)
            v1[v5].append(v4)
            v3.add((v4, v5))
        v6 = [False] * a1
        v7 = deque([0])
        v6[0] = True
        v8 = 0
        while v7:
            v9 = v7.popleft()
            for v10 in v1[v9]:
                if not v6[v10]:
                    v6[v10] = True
                    v7.append(v10)
                    if (v9, v10) in v3:
                        v8 += 1
        return v8
