class C1(object):

    def shortestWordDistance(self, a1, a2, a3):
        v1 = float('inf')
        v2 = a2 == a3
        v3, v4, v5 = (0, None, None)
        while v3 < len(a1):
            if a1[v3] == a2:
                if v2 and v4 is not None:
                    v1 = min(v1, abs(v4 - v3))
                v4 = v3
            elif a1[v3] == a3:
                v5 = v3
            if v4 is not None and v5 is not None:
                v1 = min(v1, abs(v4 - v5))
            v3 += 1
        return v1
