import collections
import random

class C1(object):

    def __init__(self):
        self.__lookup = collections.Counter()

    def addScore(self, a1, a2):
        """
        """
        self.__lookup[a1] += a2

    def top(self, a1):
        """
        """

        def kthElement(a1, a2, a3):

            def PartitionAroundPivot(a1, a2, a3, a4, a5):
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
                v4 = PartitionAroundPivot(v1, v2, v3, a1, a3)
                if v4 == a2:
                    return
                elif v4 > a2:
                    v2 = v4 - 1
                else:
                    v1 = v4 + 1
        v1 = list(self.__lookup.values())
        kthElement(v1, a1, lambda a, b: a > b)
        return sum(v1[:a1])

    def reset(self, a1):
        """
        """
        self.__lookup[a1] = 0
