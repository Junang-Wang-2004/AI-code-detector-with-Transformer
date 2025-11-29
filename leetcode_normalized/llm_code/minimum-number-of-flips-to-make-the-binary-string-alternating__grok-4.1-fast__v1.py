class C1:

    def minFlips(self, a1: str) -> int:
        v1 = len(a1)
        v2 = 0
        v3 = 0
        for v4 in range(v1):
            v5 = v4 % 2
            v6 = 1 ^ v4 % 2
            if int(a1[v4]) != v5:
                v2 += 1
            if int(a1[v4]) != v6:
                v3 += 1
        return min(v2, v3)
