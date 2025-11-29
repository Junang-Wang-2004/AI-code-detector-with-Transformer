class C1:

    def partitionArray(self, a1, a2):
        v1 = len(a1)
        if v1 % a2 != 0:
            return False
        v2 = v1 // a2
        v3 = {}
        for v4 in a1:
            v3[v4] = v3.get(v4, 0) + 1
        return max(v3.values()) <= v2
