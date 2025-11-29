class C1(object):

    def splitArraySameAverage(self, a1):
        v1 = len(a1)
        v2 = sum(a1)
        v3 = v1 // 2
        if not any((v2 * k % v1 == 0 for v4 in range(1, v3 + 1))):
            return False
        v5 = {0: {0}}
        for v6 in a1:
            v7 = {}
            for v8, v9 in list(v5.items()):
                for v10 in v9:
                    v11 = v8 + 1
                    if v11 > v3:
                        continue
                    if v11 not in v7:
                        v7[v11] = set()
                    v7[v11].add(v10 + v6)
            for v11, v12 in v7.items():
                if v11 not in v5:
                    v5[v11] = set()
                v5[v11].update(v12)
        for v13 in range(1, v3 + 1):
            if v2 * v13 % v1 == 0:
                v14 = v2 * v13 // v1
                if v14 in v5.get(v13, set()):
                    return True
        return False
