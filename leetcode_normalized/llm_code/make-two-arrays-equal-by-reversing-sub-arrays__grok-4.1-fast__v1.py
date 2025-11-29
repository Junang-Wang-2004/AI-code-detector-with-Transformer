class C1:

    def canBeEqual(self, a1, a2):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        for v2 in a2:
            if v2 not in v1 or v1[v2] == 0:
                return False
            v1[v2] -= 1
        return True
