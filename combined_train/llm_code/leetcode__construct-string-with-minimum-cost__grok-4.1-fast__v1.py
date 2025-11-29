class C1:

    def __init__(self):
        self.children = {}
        self.cost = float('inf')

class C2:

    def minimumCost(self, a1, a2, a3):
        v1 = C1()
        for v2, v3 in zip(a2, a3):
            v4 = v1
            for v5 in v2:
                if v5 not in v4.children:
                    v4.children[v5] = C1()
                v4 = v4.children[v5]
            v4.cost = min(v4.cost, v3)
        v6 = len(a1)
        v7 = [float('inf')] * (v6 + 1)
        v7[0] = 0
        for v8 in range(v6):
            if v7[v8] == float('inf'):
                continue
            v4 = v1
            for v9 in range(v8, v6):
                v5 = a1[v9]
                if v5 not in v4.children:
                    break
                v4 = v4.children[v5]
                v7[v9 + 1] = min(v7[v9 + 1], v7[v8] + v4.cost)
        return v7[v6] if v7[v6] != float('inf') else -1
