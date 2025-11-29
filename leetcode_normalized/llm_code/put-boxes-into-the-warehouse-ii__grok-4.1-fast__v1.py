class C1:

    def maxBoxesInWarehouse(self, a1, a2):
        a1.sort(key=lambda x: -x)
        v1, v2 = (0, len(a2) - 1)
        v3 = 0
        for v4 in a1:
            if v1 > v2:
                break
            if v4 <= a2[v1]:
                v1 += 1
                v3 += 1
            elif v4 <= a2[v2]:
                v2 -= 1
                v3 += 1
        return v3
