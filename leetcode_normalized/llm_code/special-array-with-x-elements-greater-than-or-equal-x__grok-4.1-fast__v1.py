class C1:

    def specialArray(self, a1):
        v1 = len(a1)
        for v2 in range(v1 + 1):
            v3 = sum((1 for v4 in a1 if v4 >= v2))
            if v3 == v2:
                return v2
        return -1
