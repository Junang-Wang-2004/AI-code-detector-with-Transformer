class C1(object):

    def shortestWordDistance(self, a1, a2, a3):
        v1 = float('inf')
        v2 = v3 = -1
        if a2 == a3:
            for v4, v5 in enumerate(a1):
                if v5 == a2:
                    if v2 > -1:
                        v1 = min(v1, v4 - v2)
                    v2 = v4
        else:
            for v4, v5 in enumerate(a1):
                if v5 == a2:
                    if v3 > -1:
                        v1 = min(v1, v4 - v3)
                    v2 = v4
                elif v5 == a3:
                    if v2 > -1:
                        v1 = min(v1, v4 - v2)
                    v3 = v4
        return v1
