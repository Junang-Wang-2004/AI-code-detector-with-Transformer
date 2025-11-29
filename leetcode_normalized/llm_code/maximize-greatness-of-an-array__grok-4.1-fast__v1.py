class C1:

    def maximizeGreatness(self, a1):
        a1.sort()
        v1 = len(a1)
        if v1 <= 1:
            return 0
        v2 = 1
        v3 = 1
        for v4 in range(1, v1):
            if a1[v4] == a1[v4 - 1]:
                v3 += 1
            else:
                v2 = max(v2, v3)
                v3 = 1
        v2 = max(v2, v3)
        return v1 - v2
