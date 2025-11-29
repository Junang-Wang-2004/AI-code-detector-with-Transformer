from collections import defaultdict, deque

class C1:

    def sortItems(self, a1, a2, a3, a4):
        v1 = a3[:]
        v2 = a2
        for v3 in range(a1):
            if v1[v3] == -1:
                v1[v3] = v2
                v2 += 1
        v4 = [[] for v5 in range(v2)]
        for v3 in range(a1):
            v4[v1[v3]].append(v3)
        v6 = defaultdict(set)
        v7 = defaultdict(int)
        v8 = [defaultdict(set) for v5 in range(v2)]
        v9 = [defaultdict(int) for v5 in range(v2)]
        for v3 in range(a1):
            v10 = v1[v3]
            for v11 in a4[v3]:
                v12 = v1[v11]
                if v10 == v12:
                    if v3 not in v8[v10][v11]:
                        v8[v10][v11].add(v3)
                        v9[v10][v3] += 1
                elif v10 not in v6[v12]:
                    v6[v12].add(v10)
                    v7[v10] += 1

        def kahn(a1, a2, a3):
            v1 = deque((nd for v2 in a3 if a2[v2] == 0))
            v3 = []
            while v1:
                v2 = v1.popleft()
                v3.append(v2)
                for v4 in a1[v2]:
                    a2[v4] -= 1
                    if a2[v4] == 0:
                        v1.append(v4)
            return v3 if len(v3) == len(a3) else None
        v13 = list(range(v2))
        v14 = kahn(v6, v7, v13)
        if v14 is None:
            return []
        v15 = []
        for v16 in v14:
            v17 = v4[v16]
            v18 = kahn(v8[v16], v9[v16], v17)
            if v18 is None:
                return []
            v15.extend(v18)
        return v15
