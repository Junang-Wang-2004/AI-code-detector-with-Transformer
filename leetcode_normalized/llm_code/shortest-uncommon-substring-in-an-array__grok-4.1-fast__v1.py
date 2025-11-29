class C1:

    def __init__(self):
        self.children = {}
        self.count = 0

class C2:

    def __init__(self):
        self.root = C1()

    def update(self, a1, a2):
        for v1 in range(len(a1)):
            v2 = self.root
            for v3 in range(v1, len(a1)):
                v4 = a1[v3]
                if v4 not in v2.children:
                    v2.children[v4] = C1()
                v2 = v2.children[v4]
                v2.count += a2

    def shortest_unique(self, a1):
        v1 = (float('inf'), '')
        for v2 in range(len(a1)):
            v3 = self.root
            for v4 in range(v2, len(a1)):
                v5 = a1[v4]
                v3 = v3.children[v5]
                v6 = v4 - v2 + 1
                if v3.count == 0:
                    v7 = (v6, a1[v2:v4 + 1])
                    if v7 < v1:
                        v1 = v7
                    break
        return v1[1]

class C3:

    def shortestSubstrings(self, a1):
        v1 = C2()
        for v2 in a1:
            v1.update(v2, 1)
        v3 = []
        for v2 in a1:
            v1.update(v2, -1)
            v3.append(v1.shortest_unique(v2))
            v1.update(v2, 1)
        return v3
