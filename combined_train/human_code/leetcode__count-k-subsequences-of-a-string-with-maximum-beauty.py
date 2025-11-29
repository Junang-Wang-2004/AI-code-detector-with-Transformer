import collections
import random
from functools import reduce

class C1(object):

    def countKSubsequencesWithMaxBeauty(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3, v4 = [[1] * 2 for v5 in range(3)]

        def nCr(a1, a2):
            if not 0 <= a2 <= a1:
                return 0
            while len(v3) <= a1:
                v2.append(v2[-1] * len(v3) % v1)
                v3.append(v3[v1 % len(v3)] * (v1 - v1 // len(v3)) % v1)
                v4.append(v4[-1] * v3[-1] % v1)
            return v2[a1] * v4[a1 - a2] % v1 * v4[a2] % v1

        def nth_element(a1, a2, a3=lambda a, b: a < b):

            def tri_partition(a1, a2, a3, a4, a5):
                v1 = a2
                while v1 <= a3:
                    if a1[v1] == a4:
                        v1 += 1
                    elif a5(a1[v1], a4):
                        a1[a2], a1[v1] = (a1[v1], a1[a2])
                        a2 += 1
                        v1 += 1
                    else:
                        a1[v1], a1[a3] = (a1[a3], a1[v1])
                        a3 -= 1
                return (a2, a3)
            v1, v2 = (0, len(a1) - 1)
            while v1 <= v2:
                v3 = random.randint(v1, v2)
                v4, v5 = tri_partition(a1, v1, v2, a1[v3], a3)
                if v4 <= a2 <= v5:
                    return
                elif v4 > a2:
                    v2 = v4 - 1
                else:
                    v1 = v5 + 1
        v6 = collections.Counter(a1)
        if len(v6) < a2:
            return 0
        v7 = list(v6.values())
        nth_element(v7, a2 - 1, lambda a, b: a > b)
        v8 = v7.count(v7[a2 - 1])
        v9 = sum((v7[i] == v7[a2 - 1] for v10 in range(a2)))
        return reduce(lambda a, b: a * b % v1, (v7[v10] for v10 in range(a2)), 1) * nCr(v8, v9) % v1
