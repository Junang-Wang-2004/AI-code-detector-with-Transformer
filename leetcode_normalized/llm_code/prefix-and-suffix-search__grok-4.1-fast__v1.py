class C1:

    def __init__(self):
        self.children = {}
        self.indices = []

class C2:

    def __init__(self):
        self.root = C1()

    def insert(self, a1, a2):
        v1 = self.root
        v1.indices.append(a2)
        for v2 in a1:
            if v2 not in v1.children:
                v1.children[v2] = C1()
            v1 = v1.children[v2]
            v1.indices.append(a2)

    def collect(self, a1):
        v1 = self.root
        for v2 in a1:
            if v2 not in v1.children:
                return []
            v1 = v1.children[v2]
        return v1.indices

class C3:

    def __init__(self, a1):
        self.pt = C2()
        self.st = C2()
        v1 = len(a1)
        for v2 in range(v1 - 1, -1, -1):
            self.pt.insert(a1[v2], v2)
            self.st.insert(a1[v2][::-1], v2)

    def f(self, a1, a2):
        v1 = self.pt.collect(a1)
        v2 = self.st.collect(a2[::-1])
        v3, v4 = (0, 0)
        while v3 < len(v1) and v4 < len(v2):
            if v1[v3] == v2[v4]:
                return v1[v3]
            elif v1[v3] > v2[v4]:
                v3 += 1
            else:
                v4 += 1
        return -1
