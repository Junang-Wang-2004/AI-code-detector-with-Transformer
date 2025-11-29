class C1(object):

    def minMoves(self, a1, a2, a3, a4):
        v1, v2 = (a1, a2)
        v3, v4 = (a3, a4)
        v5 = 0
        while v3 != v1 or v4 != v2:
            if v3 < v1 or v4 < v2:
                return -1
            if v3 == v4:
                if v1 == 0:
                    v3 = 0
                elif v2 == 0:
                    v4 = 0
                else:
                    return -1
            elif v3 < v4:
                v6 = v4 // 2
                if v3 > v6:
                    v4 -= v3
                else:
                    if v4 % 2:
                        return -1
                    v4 = v6
            else:
                v6 = v3 // 2
                if v4 > v6:
                    v3 -= v4
                else:
                    if v3 % 2:
                        return -1
                    v3 = v6
            v5 += 1
        return v5
