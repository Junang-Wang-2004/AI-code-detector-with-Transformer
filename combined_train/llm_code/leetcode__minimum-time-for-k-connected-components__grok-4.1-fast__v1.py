class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.size = [1] * a1

    def find(self, a1):
        v1 = a1
        while self.parent[v1] != v1:
            v1 = self.parent[v1]
        while a1 != v1:
            v2 = self.parent[a1]
            self.parent[a1] = v1
            a1 = v2
        return v1

    def unite(self, a1, a2):
        v1 = self.find(a1)
        v2 = self.find(a2)
        if v1 == v2:
            return False
        if self.size[v1] < self.size[v2]:
            v1, v2 = (v2, v1)
        self.parent[v2] = v1
        self.size[v1] += self.size[v2]
        return True

class C2:

    def minTime(self, a1, a2, a3):
        a2.sort(key=lambda e: -e[2])
        v1 = C1(a1)
        v2 = a1
        for v3, v4, v5 in a2:
            if v1.find(v3) != v1.find(v4):
                if v2 == a3:
                    return v5
                v1.unite(v3, v4)
                v2 -= 1
        return 0
