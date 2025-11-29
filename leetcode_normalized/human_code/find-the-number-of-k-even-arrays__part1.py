import collections

class C1(object):

    def countOfArrays(self, a1, a2, a3):
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

        def nHr(a1, a2):
            return nCr(a1 + a2 - 1, a2)
        v6 = collections.defaultdict(list)

        def pow(a1, a2):
            while len(v6[a1]) <= a2:
                v6[a1].append(v6[a1][-1] * a1 % v1 if v6[a1] else 1)
            return v6[a1][a2]
        v1 = 10 ** 9 + 7
        v7, v8 = (a2 // 2, (a2 + 1) // 2)
        v9 = 0
        if a3 == 0:
            v9 = (v9 + pow(v8, a1)) % v1
        for v10 in range(1, (a1 + 1 - a3) // 2 + 1):
            v9 = (v9 + nHr(v10, a3 + v10 - v10) * nHr(v10 + 1, a1 - (a3 + v10) - (v10 + 1 - 2)) * pow(v7, a3 + v10) * pow(v8, a1 - (a3 + v10)) % v1) % v1
        return v9
