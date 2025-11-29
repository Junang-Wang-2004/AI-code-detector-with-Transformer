from functools import reduce

class C1(object):

    def countBalancedPermutations(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3, v4 = [[1] * 2 for v5 in range(3)]

        def lazy_init(a1):
            while len(v3) <= a1:
                v2.append(v2[-1] * len(v3) % v1)
                v3.append(v3[v1 % len(v3)] * (v1 - v1 // len(v3)) % v1)
                v4.append(v4[-1] * v3[-1] % v1)

        def nCr(a1, a2):
            lazy_init(a1)
            return v2[a1] * v4[a1 - a2] % v1 * v4[a2] % v1

        def factorial(a1):
            lazy_init(a1)
            return v2[a1]

        def inv_factorial(a1):
            lazy_init(a1)
            return v4[a1]
        v6 = sum((ord(x) - ord('0') for v7 in a1))
        if v6 % 2:
            return 0
        v6 //= 2
        v8 = [0] * 10
        for v7 in a1:
            v8[ord(v7) - ord('0')] += 1
        v9 = len(a1) // 2
        v10 = [[0] * (v9 + 1) for v5 in range(v6 + 1)]
        v10[0][0] = 1
        for v11, v7 in enumerate(v8):
            if not v7:
                continue
            for v12 in reversed(range(v6 + 1)):
                for v13 in reversed(range(v9 + 1)):
                    if not v10[v12][v13]:
                        continue
                    for v14 in range(1, v7 + 1):
                        if v12 + v14 * v11 <= v6 and v13 + v14 <= v9:
                            v10[v12 + v14 * v11][v13 + v14] = (v10[v12 + v14 * v11][v13 + v14] + v10[v12][v13] * nCr(v7, v14)) % v1
        return v10[v6][v9] * factorial(v9) * factorial(len(a1) - v9) * reduce(lambda accu, x: accu * v7 % v1, (inv_factorial(v7) for v7 in v8), 1) % v1
