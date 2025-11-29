from collections import deque

class C1:

    def assignEdgeWeights(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1) + 1
        v3 = [[] for v4 in range(v2)]
        for v5, v6 in a1:
            v5 -= 1
            v6 -= 1
            v3[v5].append(v6)
            v3[v6].append(v5)
        v7 = [-1] * v2
        v7[0] = 0
        v8 = deque([0])
        while v8:
            v9 = v8.popleft()
            for v10 in v3[v9]:
                if v7[v10] == -1:
                    v7[v10] = v7[v9] + 1
                    v8.append(v10)
        v11 = max(v7)
        return pow(2, v11 - 1, v1)
