class C1:

    def __init__(self):
        self.children = [None] * 2

class C2:

    def __init__(self, a1):
        self.root = C1()
        self.bits = a1

    def insert(self, a1):
        v1 = self.root
        for v2 in range(self.bits - 1, -1, -1):
            v3 = a1 >> v2 & 1
            if not v1.children[v3]:
                v1.children[v3] = C1()
            v1 = v1.children[v3]

    def get_max_xor(self, a1):
        if not self.root.children[0] and (not self.root.children[1]):
            return 0
        v1 = self.root
        v2 = 0
        for v3 in range(self.bits - 1, -1, -1):
            v4 = a1 >> v3 & 1
            v5 = 1 - v4
            if v1.children[v5]:
                v2 |= 1 << v3
                v1 = v1.children[v5]
            else:
                v1 = v1.children[v4]
        return v2

class C3:

    def maxXor(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0] * a1

        def calc(a1, a2):
            v1 = a3[a1]
            for v2 in v1[a1]:
                if v2 != a2:
                    v1 += calc(v2, a1)
            v5[a1] = v1
            return v1
        calc(0, -1)
        if a1 == 1:
            return 0
        v6 = max(v5).bit_length()
        v7 = C2(v6)

        def search(a1, a2):
            v1 = v7.get_max_xor(v5[a1])
            for v2 in v1[a1]:
                if v2 != a2:
                    v1 = max(v1, search(v2, a1))
            v7.insert(v5[a1])
            return v1
        return search(0, -1)
