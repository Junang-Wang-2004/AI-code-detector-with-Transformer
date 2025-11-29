import collections

class C1(object):

    def colorTheGrid(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def normalize(a1, a2, a3):
            if a2 not in a3[a1]:
                v1 = {}
                v2, v3 = (0, a1)
                while v3:
                    v4 = a2 // v3 % 3
                    if v4 not in v1:
                        v1[v4] = len(v1)
                    v2 += v1[v4] * v3
                    v3 //= 3
                a3[a1][a2] = v2
            return a3[a1][a2]
        if a1 > a2:
            a1, a2 = (a2, a1)
        v4 = v5 = 3 ** (a1 - 1)
        v6 = collections.defaultdict(dict)
        v7 = collections.Counter({0: 1})
        for v8 in range(a1 * a2):
            v9, v10 = divmod(v8, a1)
            assert v9 != 0 or v10 != 0 or len(v7) == 1
            assert v9 != 0 or v10 == 0 or len(v7) == 3 * 2 ** (v10 - 1) // 3 // (2 if v10 >= 2 else 1)
            assert v9 == 0 or v10 != 0 or len(v7) == 3 * 2 ** (a1 - 1) // 3 // (2 if a1 >= 2 else 1)
            assert v9 == 0 or v10 == 0 or len(v7) == (1 if a1 == 1 else 2 if a1 == 2 else 3 * 3 * 2 ** (a1 - 2) // 3 // 2)
            v11 = collections.Counter()
            for v12, v13 in v7.items():
                v14 = {0, 1, 2}
                if v9 > 0:
                    v14.discard(v12 % 3)
                if v10 > 0:
                    v14.discard(v12 // v4)
                for v15 in v14:
                    v16 = normalize(v4 // v5, (v15 * v4 + v12 // 3) // v5, v6) * v5
                    v11[v16] = (v11[v16] + v13) % v1
            if v5 > 1:
                v5 //= 3
            v7 = v11
        return reduce(lambda x, y: (v15 + y) % v1, iter(v7.values()), 0)
