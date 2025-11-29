from functools import reduce

class C1(object):

    def magicalSum(self, a1, a2, a3):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')
        v1 = 10 ** 9 + 7
        v2, v3, v4 = [[1] * 2 for v5 in range(3)]

        def nCr(a1, a2):
            while len(v3) <= a1:
                v2.append(v2[-1] * len(v3) % v1)
                v3.append(v3[v1 % len(v3)] * (v1 - v1 // len(v3)) % v1)
                v4.append(v4[-1] * v3[-1] % v1)
            return v2[a1] * v4[a1 - a2] % v1 * v4[a2] % v1
        v6 = [[[0] * (a1 + 1) for v5 in range(a2 + 1)] for v5 in range(a1 + 1)]
        v6[0][0][a1] = 1
        for v7 in a3:
            v8 = [[[0] * (a1 + 1) for v5 in range(a2 + 1)] for v5 in range(a1 + 1)]
            for v9 in range(a1 + 1):
                for v10 in range(a2 + 1):
                    for v11 in range(a1 + 1):
                        if not v6[v9][v10][v11]:
                            continue
                        v12 = 1
                        for v13 in range(v11 + 1):
                            v14, v15, v16 = (v9 + v13 >> 1, v10 + (v9 + v13 & 1), v11 - v13)
                            if v15 > a2:
                                continue
                            v8[v14][v15][v16] = (v8[v14][v15][v16] + v6[v9][v10][v11] * v12 * nCr(v11, v13)) % v1
                            v12 = v12 * v7 % v1
            v6 = v8
        return reduce(lambda accu, x: (accu + v7) % v1, (v6[v9][a2 - popcount(v9)][0] for v9 in range(a1 + 1) if a2 - popcount(v9) >= 0), 0)
