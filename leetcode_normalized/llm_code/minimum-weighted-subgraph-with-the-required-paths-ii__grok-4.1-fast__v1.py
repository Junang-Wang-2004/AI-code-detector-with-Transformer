from typing import List

class C1:

    def __init__(self, a1: int):
        self.parent = list(range(a1))
        self.rank = [0] * a1

    def find(self, a1: int) -> int:
        if self.parent[a1] != a1:
            self.parent[a1] = self.find(self.parent[a1])
        return self.parent[a1]

    def unite(self, a1: int, a2: int) -> bool:
        v1 = self.find(a1)
        v2 = self.find(a2)
        if v1 == v2:
            return False
        if self.rank[v1] < self.rank[v2]:
            self.parent[v1] = v2
        elif self.rank[v1] > self.rank[v2]:
            self.parent[v2] = v1
        else:
            self.parent[v2] = v1
            self.rank[v1] += 1
        return True

class C2:

    def minimumWeight(self, a1: List[List[int]], a2: List[List[int]]) -> List[int]:
        v1 = len(a1) + 1
        v2 = [[] for v3 in range(v1)]
        for v4, v5, v6 in a1:
            v2[v4].append((v5, v6))
            v2[v5].append((v4, v6))
        v7 = len(a2)
        v8 = [[] for v3 in range(v1)]
        for v9, v10 in enumerate(a2):
            for v11 in v10:
                v8[v11].append(v9)
        v12 = C1(v1)
        v13 = [0] * v1
        v14 = [0] * v1
        v15 = [False] * v1
        v16 = [0] * v7

        def traverse(a1: int) -> None:
            for v1 in v8[a1]:
                v16[v1] += v14[a1]
                for v2 in a2[v1]:
                    if v15[v2]:
                        v16[v1] -= v14[v13[v12.find(v2)]]
            v15[a1] = True
            for v3, v4 in v2[a1]:
                if v15[v3]:
                    continue
                v14[v3] = v14[a1] + v4
                traverse(v3)
                v12.unite(v3, a1)
                v13[v12.find(a1)] = a1
        traverse(0)
        return v16
