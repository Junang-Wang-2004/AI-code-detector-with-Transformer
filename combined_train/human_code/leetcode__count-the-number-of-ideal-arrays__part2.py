import collections

class C1(object):

    def idealArrays(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3, v4 = [[1] * 2 for v5 in range(3)]

        def nCr(a1, a2):
            while len(v3) <= a1:
                v2.append(v2[-1] * len(v3) % v1)
                v3.append(v3[v1 % len(v3)] * (v1 - v1 // len(v3)) % v1)
                v4.append(v4[-1] * v3[-1] % v1)
            return v2[a1] * v4[a1 - a2] % v1 * v4[a2] % v1
        v6 = 0
        v7 = collections.Counter(range(1, a2 + 1))
        for v8 in range(a1):
            v9 = collections.Counter()
            v10 = 0
            for v11, v12 in v7.items():
                v10 = (v10 + v12) % v1
                for v13 in range(v11 + v11, a2 + 1, v11):
                    v9[v13] += v12
            v6 = (v6 + v10 * nCr(a1 - 1, v8)) % v1
            v7 = v9
        return v6
