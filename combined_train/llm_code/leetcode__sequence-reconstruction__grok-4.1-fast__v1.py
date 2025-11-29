from collections import deque, defaultdict

class C1:

    def sequenceReconstruction(self, a1, a2):
        v1 = len(a1)
        v2 = set(a1)
        v3 = defaultdict(list)
        v4 = {num: 0 for v5 in v2}
        v6 = set()
        for v7 in a2:
            for v8 in v7:
                if v8 not in v2:
                    return False
                v6.add(v8)
            for v9 in range(len(v7) - 1):
                v10 = v7[v9]
                v11 = v7[v9 + 1]
                if v11 not in v3[v10]:
                    v3[v10].append(v11)
                    v4[v11] += 1
        if len(v6) != v1:
            return False
        v12 = deque([nd for v13 in v2 if v4[v13] == 0])
        if len(v12) != 1:
            return False
        v14 = []
        while v12:
            if len(v12) != 1:
                return False
            v15 = v12.popleft()
            v14.append(v15)
            for v16 in v3[v15]:
                v4[v16] -= 1
                if v4[v16] == 0:
                    v12.append(v16)
        return v14 == a1
