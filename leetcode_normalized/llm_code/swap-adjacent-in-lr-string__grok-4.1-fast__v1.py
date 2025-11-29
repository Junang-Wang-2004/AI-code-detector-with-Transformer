class C1:

    def canTransform(self, a1: str, a2: str) -> bool:
        v1 = ''.join((c for v2 in a1 if v2 != 'X'))
        v3 = ''.join((v2 for v2 in a2 if v2 != 'X'))
        if v1 != v3:
            return False
        v4 = [idx for v5, v2 in enumerate(a1) if v2 != 'X']
        v6 = [v5 for v5, v2 in enumerate(a2) if v2 != 'X']
        v7 = len(v4)
        for v8 in range(v7):
            if v1[v8] == 'L' and v4[v8] < v6[v8]:
                return False
            if v1[v8] == 'R' and v4[v8] > v6[v8]:
                return False
        return True
