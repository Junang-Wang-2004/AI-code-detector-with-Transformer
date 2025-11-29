from collections import deque

class C1:

    def maxHammingDistances(self, a1, a2):
        v1 = 1 << a2
        v2 = [-1] * v1
        v3 = deque()
        v4 = set()
        v5 = v1 - 1
        for v6 in a1:
            if v6 not in v4:
                v4.add(v6)
                v2[v6] = 0
                v3.append(v6)
        while v3:
            v7 = v3.popleft()
            for v8 in range(a2):
                v9 = v7 ^ 1 << v8
                if v2[v9] == -1:
                    v2[v9] = v2[v7] + 1
                    v3.append(v9)
        v10 = []
        for v6 in a1:
            v11 = v5 ^ v6
            v10.append(a2 - v2[v11])
        return v10
