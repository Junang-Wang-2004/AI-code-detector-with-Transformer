from collections import deque

class C1:

    def secondMinimum(self, a1, a2, a3, a4):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3 - 1].append(v4 - 1)
            v1[v4 - 1].append(v3 - 1)

        def shortest_distances(a1):
            v1 = [-1] * a1
            v1[a1] = 0
            v2 = deque([a1])
            while v2:
                v3 = v2.popleft()
                for v4 in v1[v3]:
                    if v1[v4] == -1:
                        v1[v4] = v1[v3] + 1
                        v2.append(v4)
            return v1
        v5 = shortest_distances(0)
        v6 = v5[a1 - 1]
        v7 = shortest_distances(a1 - 1)
        v8 = v6 + 2
        for v9 in range(a1):
            v10 = v5[v9] + v7[v9]
            if v10 > v6:
                v8 = min(v8, v10)
        v11 = 0
        for v2 in range(v8):
            if v11 // a4 % 2 == 1:
                v11 = (v11 // a4 + 1) * a4
            v11 += a3
        return v11
