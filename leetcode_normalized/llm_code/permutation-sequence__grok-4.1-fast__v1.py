class C1(object):

    def getPermutation(self, a1, a2):
        a2 -= 1
        v2 = [1] * (a1 + 1)
        for v3 in range(1, a1 + 1):
            v2[v3] = v2[v3 - 1] * v3
        v4 = 0
        v5 = []
        for v6 in range(a1 - 1, -1, -1):
            v7 = v2[v6]
            v8 = a2 // v7
            a2 %= v7
            v9 = 0
            for v10 in range(1, a1 + 1):
                v11 = 1 << v10 - 1
                if v4 & v11 == 0:
                    if v9 == v8:
                        v5.append(str(v10))
                        v4 |= v11
                        break
                    v9 += 1
        return ''.join(v5)
