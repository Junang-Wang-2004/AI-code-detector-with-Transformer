from collections import defaultdict, deque

class C1:

    def frogPosition(self, a1, a2, a3, a4):
        v1 = defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        if a4 not in v1:
            return 0.0
        v4 = {}
        v5 = {}
        v6 = deque([1])
        v4[1] = None
        v5[1] = 0
        while v6:
            v7 = v6.popleft()
            if v7 == a4:
                break
            for v8 in v1[v7]:
                if v8 != v4.get(v7):
                    v4[v8] = v7
                    v5[v8] = v5[v7] + 1
                    v6.append(v8)
        if a4 not in v5:
            return 0.0
        v9 = v5[a4]
        if v9 > a3:
            return 0.0
        v10 = len(v1[a4]) - (0 if v4.get(a4) is None else 1)
        if v9 < a3 and v10 > 0:
            return 0.0
        v11 = 1.0
        v12 = a4
        while v12 != 1:
            v13 = v4[v12]
            v14 = len(v1[v13]) - (0 if v13 == 1 else 1)
            v11 /= v14
            v12 = v13
        return v11
