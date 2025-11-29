class C1(object):

    def shortestDistance(self, a1, a2, a3):
        v1 = float('inf')
        v2, v3, v4 = (0, None, None)
        while v2 < len(a1):
            if a1[v2] == a2:
                v3 = v2
            elif a1[v2] == a3:
                v4 = v2
            if v3 is not None and v4 is not None:
                v1 = min(v1, abs(v3 - v4))
            v2 += 1
        return v1
