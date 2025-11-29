class C1:

    def search(self, a1, a2):
        v1, v2 = (0, 19999)
        while v1 <= v2:
            v3 = (v1 + v2) // 2
            v4 = a1.get(v3)
            if v4 == a2:
                return v3
            elif v4 < a2:
                v1 = v3 + 1
            else:
                v2 = v3 - 1
        return -1
