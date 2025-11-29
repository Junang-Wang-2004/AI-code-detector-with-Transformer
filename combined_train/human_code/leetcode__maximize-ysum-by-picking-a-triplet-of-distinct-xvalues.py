import collections
import itertools
import random

class C1(object):

    def maxSumDistinctTriplet(self, a1, a2):
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
        v1 = 3
        v2 = collections.defaultdict(int)
        for v3, v4 in zip(a1, a2):
            v2[v3] = max(v2[v3], v4)
        if len(v2) < v1:
            return -1
        v5 = list(v2.values())
        nth_element(v5, v1 - 1, compare=lambda x, y: a1 > a2)
        return sum((v5[v3] for v3 in range(v1)))
