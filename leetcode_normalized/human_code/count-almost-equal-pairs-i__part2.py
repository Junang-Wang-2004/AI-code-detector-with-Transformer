import collections

class C1(object):

    def countPairs(self, a1):
        """
        """
        v1 = 7
        v2 = 1
        v3 = [0] * v1
        v3[0] = 1
        for v4 in range(v1 - 1):
            v3[v4 + 1] = v3[v4] * 10

        def at_most(a1, a2):
            v1 = {a2}
            v2 = [a2]
            v3 = 0
            for v4 in range(a1):
                for v3 in range(v3, len(v2)):
                    a2 = v2[v3]
                    for v6 in range(v1):
                        v7 = a2 // v3[v6] % 10
                        for v8 in range(v6 + 1, v1):
                            v9 = a2 // v3[v8] % 10
                            if v7 == v9:
                                continue
                            v10 = a2 - v7 * (v3[v6] - v3[v8]) + v9 * (v3[v6] - v3[v8])
                            if v10 in v1:
                                continue
                            v1.add(v10)
                            v2.append(v10)
            return v2
        v5 = 0
        v6 = collections.Counter(a1)
        v7 = collections.Counter()
        for v8, v9 in v6.items():
            v5 += v7[v8] * v9 + v9 * (v9 - 1) // 2
            for v8 in at_most(v2, v8):
                if v8 not in v6:
                    continue
                v7[v8] += v9
        return v5
