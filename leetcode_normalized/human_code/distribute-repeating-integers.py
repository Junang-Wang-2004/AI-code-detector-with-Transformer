import collections
import random

class C1(object):

    def canDistribute(self, a1, a2):
        """
        """

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
        v1 = collections.Counter(a1)
        v2 = (1 << len(a2)) - 1
        v3 = [0] * (v2 + 1)
        for v4 in range(len(v3)):
            v5 = 1
            for v6 in range(len(a2)):
                if v4 & v5:
                    v3[v4] += a2[v6]
                v5 <<= 1
        v7 = [[0] * (v2 + 1) for v8 in range(2)]
        v7[0][0] = 1
        v6 = 0
        v9 = list(v1.values())
        if len(a2) < len(v9):
            nth_element(v9, len(a2) - 1, lambda a, b: a > b)
            v9 = v9[:len(a2)]
        for v10 in v9:
            v7[(v6 + 1) % 2] = [0] * (v2 + 1)
            for v4 in reversed(range(v2 + 1)):
                v7[(v6 + 1) % 2][v4] |= v7[v6 % 2][v4]
                v11 = v4
                while v11 > 0:
                    if v3[v11] <= v10 and v7[v6 % 2][v4 ^ v11]:
                        v7[(v6 + 1) % 2][v4] = 1
                    v11 = v11 - 1 & v4
            v6 += 1
        return v7[len(v9) % 2][v2]
