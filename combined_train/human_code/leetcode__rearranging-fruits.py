import random
import collections

class C1(object):

    def minCost(self, a1, a2):
        """
        """

        def nth_element(a1, a2, a3=0, a4=lambda a, b: a < b):

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
            v1 = len(a1) - 1
            while a3 <= v1:
                v2 = random.randint(a3, v1)
                v3, v4 = tri_partition(a1, a3, v1, a1[v2], a4)
                if v3 <= a2 <= v4:
                    return
                elif v3 > a2:
                    v1 = v3 - 1
                else:
                    a3 = v4 + 1
        v1 = collections.Counter()
        for v2 in a1:
            v1[v2] += 1
        for v2 in a2:
            v1[v2] -= 1
        v3 = min(v1.keys())
        v4 = []
        for v5, v6 in v1.items():
            if v6 % 2:
                return -1
            v4.extend((v5 for v7 in range(abs(v6) // 2)))
        nth_element(v4, len(v4) // 2)
        return sum((min(v4[i], v3 * 2) for v8 in range(len(v4) // 2)))
