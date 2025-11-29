import math
import random

class C1(object):

    def minimizeError(self, a1, a2):
        """
        """

        def kthElement(a1, a2, a3=lambda a, b: a < b):

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
        v1 = []
        v2, v3 = (0, 0)
        for v4, v5 in enumerate(map(float, a1)):
            v2 += int(math.floor(v5))
            v3 += int(math.ceil(v5))
            if v5 != math.floor(v5):
                v1.append(v5 - math.floor(v5))
        if not v2 <= a2 <= v3:
            return '-1'
        v6 = v3 - a2
        kthElement(v1, v6)
        v7 = 0.0
        for v4 in range(len(v1)):
            if v4 < v6:
                v7 += v1[v4]
            else:
                v7 += 1.0 - v1[v4]
        return '{:.3f}'.format(v7)
