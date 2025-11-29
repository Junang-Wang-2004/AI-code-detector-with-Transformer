import random

class C1(object):

    def getStrongest(self, a1, a2):
        """
        """

        def nth_element(a1, a2, a3=lambda a, b: a < b):

            def partition_around_pivot(a1, a2, a3, a4, a5):
                v1 = a1
                a4[a3], a4[a2] = (a4[a2], a4[a3])
                for v2 in range(a1, a2):
                    if a5(a4[v2], a4[a2]):
                        a4[v2], a4[v1] = (a4[v1], a4[v2])
                        v1 += 1
                a4[a2], a4[v1] = (a4[v1], a4[a2])
                return v1
            v1, v2 = (0, len(a1) - 1)
            while v1 <= v2:
                v3 = random.randint(v1, v2)
                v4 = partition_around_pivot(v1, v2, v3, a1, a3)
                if v4 == a2:
                    return
                elif v4 > a2:
                    v2 = v4 - 1
                else:
                    v1 = v4 + 1
        nth_element(a1, (len(a1) - 1) // 2)
        v1 = a1[(len(a1) - 1) // 2]
        nth_element(a1, a2, lambda a, b: abs(a - v1) > abs(b - v1) if abs(a - v1) != abs(b - v1) else a > b)
        return a1[:a2]
