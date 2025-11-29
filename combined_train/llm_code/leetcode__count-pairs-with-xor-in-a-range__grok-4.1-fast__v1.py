class C1:

    def __init__(self):
        self.children = [None, None]
        self.count = 0

class C2:

    def __init__(self):
        self.root = C1()

    def insert(self, a1):
        v1 = self.root
        for v2 in range(31, -1, -1):
            v3 = a1 >> v2 & 1
            if v1.children[v3] is None:
                v1.children[v3] = C1()
            v1 = v1.children[v3]
            v1.count += 1

    def query(self, a1, a2):
        if a2 < 0:
            return 0
        v1 = self.root
        v2 = 0
        for v3 in range(31, -1, -1):
            if v1 is None:
                return v2
            v4 = a1 >> v3 & 1
            v5 = a2 >> v3 & 1
            if v5 == 1:
                if v1.children[v4]:
                    v2 += v1.children[v4].count
                v6 = 1 ^ v4
                if v1.children[v6] is None:
                    return v2
                v1 = v1.children[v6]
            else:
                v6 = v4
                if v1.children[v6] is None:
                    return v2
                v1 = v1.children[v6]
        return v2

class C3:

    def countPairs(self, a1, a2, a3):
        v1 = C2()
        v2 = 0
        for v3 in a1:
            v2 += v1.query(v3, a3 + 1) - v1.query(v3, a2)
            v1.insert(v3)
        return v2
