import collections

class C1:

    def beautifulNumbers(self, a1, a2):

        def count(a1):
            if a1 < 0:
                return 0
            v1 = [int(ch) for v2 in str(a1)]
            v3 = {(1, 1, 0): 1}
            for v4 in range(len(v1)):
                v5 = v1[v4]
                v6 = collections.defaultdict(int)
                for (v7, v8, v9), v10 in v3.items():
                    v11 = v5 if v7 else 9
                    for v12 in range(v11 + 1):
                        v13 = 1 if v7 and v12 == v5 else 0
                        v14 = v8 * (1 if v9 == 0 and v12 == 0 else v12)
                        v15 = v9 + v12
                        v6[v13, v14, v15] += v10
                v3 = v6
            v16 = 0
            for (v7, v8, v9), v10 in v3.items():
                if v9 > 0 and v8 % v9 == 0:
                    v16 += v10
            return v16
        return count(a2) - count(a1 - 1)
