class C1:

    def minimumCost(self, a1):
        v1, v2 = (float('inf'), float('inf'))
        for v3 in a1[1:]:
            if v3 < v1:
                v2 = v1
                v1 = v3
            elif v3 < v2:
                v2 = v3
        return a1[0] + v1 + v2
