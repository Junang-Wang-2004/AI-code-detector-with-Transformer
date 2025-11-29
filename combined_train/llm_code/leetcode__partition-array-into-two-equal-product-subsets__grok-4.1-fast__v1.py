class C1:

    def checkEqualPartitions(self, a1, a2):
        v1 = 1
        v2 = a2 * a2
        for v3 in a1:
            v1 *= v3
            if v1 > v2:
                return False
        if v1 != v2:
            return False
        v4 = len(a1)
        v5 = 1 << v4
        for v6 in range(1, v5 - 1):
            v7 = 1
            for v8 in range(v4):
                if v6 & 1 << v8 != 0:
                    v7 *= a1[v8]
                    if v7 > a2:
                        break
            else:
                if v7 == a2:
                    return True
        return False
