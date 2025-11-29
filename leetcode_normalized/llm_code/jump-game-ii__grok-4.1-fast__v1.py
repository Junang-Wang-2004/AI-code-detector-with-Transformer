class C1:

    def jump(self, a1):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        v4 = 0
        v5 = 0
        while v2 < v1 - 1:
            if v5 > v2:
                return -1
            while v5 <= v3 and v5 < v1:
                v2 = max(v2, v5 + a1[v5])
                v5 += 1
            v3 = v2
            v4 += 1
        return v4
