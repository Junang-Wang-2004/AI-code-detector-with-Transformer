class C1:

    def countPartitions(self, a1):
        v1 = len(a1)
        if v1 < 2:
            return 0
        v2 = 0
        for v3 in a1:
            v2 = (v2 + v3) % 2
        return v1 - 1 if v2 == 0 else 0
