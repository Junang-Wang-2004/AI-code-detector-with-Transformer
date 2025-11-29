class C1(object):

    def makesquare(self, a1):
        """
        """
        v1 = sum(a1)
        if v1 % 4:
            return False
        v2 = v1 / 4
        v3 = (1 << len(a1)) - 1
        v4 = []
        v5 = [0] * (1 << len(a1))
        for v6 in range(v3 + 1):
            v7 = 0
            for v8 in range(len(a1)):
                if v6 & 1 << v8:
                    v7 += a1[v8]
            if v7 == v2:
                for v9 in v4:
                    if v9 & v6 == 0:
                        v10 = v9 | v6
                        v5[v10] = True
                        if v5[v3 ^ v10]:
                            return True
                v4.append(v6)
        return False
