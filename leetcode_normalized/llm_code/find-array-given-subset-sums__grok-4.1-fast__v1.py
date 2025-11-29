class C1(object):

    def recoverArray(self, a1, a2):
        v1 = sorted(a2)
        v2 = 0
        v3 = []
        v4 = len(v1)
        while v4 > 1:
            v5 = v1[0] - v1[1]
            v6 = []
            v7 = 0
            v8 = False
            for v9 in range(v4):
                if v7 < len(v6) and v6[v7] == v1[v9]:
                    v7 += 1
                else:
                    v10 = v1[v9] - v5
                    if v10 == v2:
                        v8 = True
                    v6.append(v10)
            if v8:
                v3.append(v5)
            else:
                v3.append(-v5)
                v2 -= v5
            v1 = v6
            v4 //= 2
        return v3
