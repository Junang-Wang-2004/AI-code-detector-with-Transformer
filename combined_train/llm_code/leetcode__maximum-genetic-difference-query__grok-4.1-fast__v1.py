from collections import defaultdict

class C1:

    def __init__(self):
        self.children = [None] * 2
        self.count = 0

class C2:

    def __init__(self, a1):
        self.bits = a1
        self.root = C1()

    def insert(self, a1, a2):
        v1 = self.root
        v1.count += a2
        for v2 in range(self.bits - 1, -1, -1):
            v3 = a1 >> v2 & 1
            if v1.children[v3] is None:
                v1.children[v3] = C1()
            v1 = v1.children[v3]
            v1.count += a2

    def get_max_xor(self, a1):
        v1 = self.root
        if v1.count == 0:
            return 0
        v2 = 0
        for v3 in range(self.bits - 1, -1, -1):
            v4 = a1 >> v3 & 1
            v5 = 1 - v4
            if v1.children[v5] is not None and v1.children[v5].count > 0:
                v2 |= 1 << v3
                v1 = v1.children[v5]
            elif v1.children[v4] is not None and v1.children[v4].count > 0:
                v1 = v1.children[v4]
            else:
                break
        return v2

class C3:

    def maxGeneticDifference(self, a1, a2):
        v1 = len(a1)
        v2 = defaultdict(list)
        v3 = next((i for v4, v5 in enumerate(a1) if v5 == -1))
        for v4, v5 in enumerate(a1):
            if v5 != -1:
                v2[v5].append(v4)
        v6 = defaultdict(list)
        v7 = v1 - 1
        for v8, (v9, v10) in enumerate(a2):
            v6[v9].append((v8, v10))
            if v10 > v7:
                v7 = v10
        v11 = v7.bit_length()
        v12 = [0] * len(a2)
        v13 = C2(v11)
        v14 = [(0, v3)]
        while v14:
            v15, v16 = v14[-1]
            if v15 == 0:
                v14[-1] = (1, v16)
                v13.insert(v16, 1)
                for v17, v10 in v6[v16]:
                    v12[v17] = v13.get_max_xor(v10)
                for v18 in reversed(v2[v16]):
                    v14.append((0, v18))
            else:
                v13.insert(v16, -1)
                v14.pop()
        return v12
