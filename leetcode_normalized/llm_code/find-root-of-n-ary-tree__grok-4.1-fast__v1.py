class C1:

    def findRoot(self, a1):
        v1 = 0
        v2 = 0
        for v3 in a1:
            v1 ^= id(v3)
        for v3 in a1:
            for v4 in v3.children:
                v2 ^= id(v4)
        v5 = v1 ^ v2
        for v3 in a1:
            if id(v3) == v5:
                return v3
        return None
