from functools import reduce

class C1(object):

    def maxHappyGroups(self, a1, a2):
        """
        """

        def memoization(a1, a2, a3, a4, a5):
            if a5[a3] == 0:
                v1 = 0
                if a4 in a2:
                    v2, v3 = (a3, 1)
                    for v4, v5 in a2.items():
                        if v4 == a4:
                            break
                        v3 *= v5 + 1
                        v2 //= v5 + 1
                    v1 = v2 % (a2[a4] + 1)
                v6 = 0
                if v1:
                    v6 = max(v6, int(a4 == 0) + memoization(a1, a2, a3 - v3, 0, a5))
                else:
                    v2, v3 = (a3, 1)
                    for v4, v5 in a2.items():
                        if v2 % (v5 + 1):
                            v6 = max(v6, int(a4 == 0) + memoization(a1, a2, a3 - v3, (a4 - v4) % a1, a5))
                        v3 *= v5 + 1
                        v2 //= v5 + 1
                a5[a3] = v6
            return a5[a3]
        v1 = [0] * a1
        for v2 in a2:
            v1[v2 % len(v1)] += 1
        v3 = v1[0]
        v1[0] = 0
        for v2 in range(1, len(v1) // 2 + 1):
            v4 = min(v1[v2], v1[len(v1) - v2]) if 2 * v2 != len(v1) else v1[v2] // 2
            v3 += v4
            v1[v2] -= v4
            v1[len(v1) - v2] -= v4
        v5 = {v2: c for v2, v6 in enumerate(v1) if v6}
        v7 = reduce(lambda total, c: total * (v6 + 1), iter(v5.values()), 1)
        v8 = [0] * v7
        return v3 + memoization(a1, v5, v7 - 1, 0, v8)
