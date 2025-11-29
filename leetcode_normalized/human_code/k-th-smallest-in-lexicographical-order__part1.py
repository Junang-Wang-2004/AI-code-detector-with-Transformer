class C1(object):

    def findKthNumber(self, a1, a2):
        """
        """
        v1 = 0
        v2 = [0] * 10
        for v3 in range(1, 10):
            v2[v3] = v2[v3 - 1] * 10 + 1
        v4 = []
        v3 = a1
        while v3:
            v4.append(v3 % 10)
            v3 /= 10
        v5, v6 = (a1, 0)
        v3 = len(v4) - 1
        while v3 >= 0 and a2 > 0:
            v6 = v6 * 10 + v4[v3]
            v7 = int(v3 == len(v4) - 1)
            for v8 in range(v7, 10):
                v9 = v1 * 10 + v8
                if v9 < v6:
                    v10 = v2[v3 + 1]
                elif v9 > v6:
                    v10 = v2[v3]
                else:
                    v10 = v5 - v2[v3 + 1] * (v8 - v7) - v2[v3] * (9 - v8)
                if a2 > v10:
                    a2 -= v10
                else:
                    v1 = v9
                    a2 -= 1
                    v5 = v10 - 1
                    break
            v3 -= 1
        return v1
