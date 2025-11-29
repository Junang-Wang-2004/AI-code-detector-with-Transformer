import collections

class C1:

    def countSubgraphsForEachDiameter(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v3 -= 1
            v4 -= 1
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0] * (a1 - 1)
        for v6 in range(1, 1 << a1):
            v7 = self.compute_diameter(v1, v6)
            if v7 > 0:
                v5[v7 - 1] += 1
        return v5

    def compute_diameter(self, a1, a2):
        v1 = len(a1)
        v2 = 0
        while v2 < v1 and a2 & 1 << v2 == 0:
            v2 += 1
        v3 = [-1] * v1
        v3[v2] = 0
        v4 = collections.deque([v2])
        v5 = 1 << v2
        v6 = v2
        v7 = 0
        while v4:
            v8 = v4.popleft()
            for v9 in a1[v8]:
                if a2 & 1 << v9 and v3[v9] == -1:
                    v3[v9] = v3[v8] + 1
                    v5 |= 1 << v9
                    v4.append(v9)
                    if v3[v9] > v7:
                        v7 = v3[v9]
                        v6 = v9
        if v5 != a2:
            return 0
        v3 = [-1] * v1
        v3[v6] = 0
        v4 = collections.deque([v6])
        v10 = 0
        while v4:
            v8 = v4.popleft()
            v10 = max(v10, v3[v8])
            for v9 in a1[v8]:
                if a2 & 1 << v9 and v3[v9] == -1:
                    v3[v9] = v3[v8] + 1
                    v4.append(v9)
        return v10
