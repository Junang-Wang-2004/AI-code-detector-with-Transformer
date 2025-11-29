class C1:

    def isConvex(self, a1):
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1):
            v4, v5 = a1[v3]
            v6, v7 = a1[(v3 + 1) % v1]
            v8, v9 = a1[(v3 + 2) % v1]
            v10 = (v6 - v4) * (v9 - v7) - (v7 - v5) * (v8 - v6)
            if v10 != 0:
                v11 = 1 if v10 > 0 else -1
                if v2 and v2 != v11:
                    return False
                v2 = v11
        return True
