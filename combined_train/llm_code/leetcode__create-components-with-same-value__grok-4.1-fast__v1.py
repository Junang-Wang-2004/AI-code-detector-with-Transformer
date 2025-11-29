class C1(object):

    def componentValue(self, a1, a2):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a2:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = sum(a1)

        def factorize(a1):
            v1 = []
            v2 = 1
            while v2 * v2 <= a1:
                if a1 % v2 == 0:
                    v1.append(v2)
                    if v2 != a1 // v2:
                        v1.append(a1 // v2)
                v2 += 1
            return sorted(set(v1), reverse=True)
        v7 = factorize(v6)

        def validate(a1):
            v1 = a1[:]
            v2 = [len(v2[j]) for v3 in range(v1)]
            v4 = [v3 for v3 in range(v1) if v2[v3] == 1]
            while v4:
                v5 = []
                for v6 in v4:
                    if v1[v6] > a1:
                        return False
                    if v1[v6] == a1:
                        v1[v6] = 0
                    for v7 in v2[v6]:
                        v1[v7] += v1[v6]
                        v2[v7] -= 1
                        if v2[v7] == 1:
                            v5.append(v7)
                v4 = v5
            return True
        for v8 in v7:
            if 2 <= v8 <= v1 and validate(v6 // v8):
                return v8 - 1
        return 0
