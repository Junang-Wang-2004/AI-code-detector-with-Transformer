import random
import itertools
import math
random.seed(0)

class C1(object):

    def beautifulPair(self, a1, a2):
        """
        """
        v1 = float('inf')

        def dist(a1, a2):
            if a1[2] > a2[2]:
                a1, a2 = (a2, a1)
            return [abs(a1[0] - a2[0]) + abs(a1[1] - a2[1]), a1[2], a2[2]]

        def cell(a1, a2):
            v1, v2, v3 = a1
            return (math.floor(v1 / a2), math.floor(v2 / a2))

        def improve():
            v1 = {}
            for v2 in points:
                v3, v4 = list(map(int, cell(v2, result[0] / 2.0)))
                for v5 in range(v3 - 2, v3 + 2 + 1):
                    for v6 in range(v4 - 2, v4 + 2 + 1):
                        if (v5, v6) not in v1:
                            continue
                        v7 = dist(v2, v1[v5, v6])
                        if v7 < result:
                            result[:] = v7
                            return True
                v1[v3, v4] = v2
            return False
        v2 = [(i, j, idx) for v3, (v4, v5) in enumerate(zip(a1, a2))]
        v6 = [v1] * 3
        v7 = {}
        for v4 in reversed(range(len(v2))):
            if v2[v4][:2] in v7:
                v6 = [0, v4, v7[v2[v4][:2]]]
            v7[v2[v4][:2]] = v4
        if v6[0] == 0:
            return v6[1:]
        random.shuffle(v2)
        v6 = dist(v2[0], v2[1])
        while improve():
            pass
        return v6[1:]
