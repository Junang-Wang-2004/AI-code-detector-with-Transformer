import random

class C1(object):

    def minDifference(self, a1):
        """
        """

        def nth_element(a1, a2, a3, a4, a5=lambda a, b: a < b):

            def partition_around_pivot(a1, a2, a3, a4, a5):
                v1 = a1
                a4[a3], a4[a2] = (a4[a2], a4[a3])
                for v2 in range(a1, a2):
                    if a5(a4[v2], a4[a2]):
                        a4[v2], a4[v1] = (a4[v1], a4[v2])
                        v1 += 1
                a4[a2], a4[v1] = (a4[v1], a4[a2])
                return v1
            while a2 <= a4:
                v1 = random.randint(a2, a4)
                v2 = partition_around_pivot(a2, a4, v1, a1, a5)
                if v2 == a3:
                    return
                elif v2 > a3:
                    a4 = v2 - 1
                else:
                    a2 = v2 + 1
        v1 = 4
        if len(a1) <= v1:
            return 0
        nth_element(a1, 0, v1, len(a1) - 1)
        a1[:v1] = sorted(a1[:v1])
        nth_element(a1, v1, max(v1, len(a1) - v1), len(a1) - 1)
        a1[-v1:] = sorted(a1[-v1:])
        return min((a1[-v1 + i] - a1[i] for v2 in range(v1)))
