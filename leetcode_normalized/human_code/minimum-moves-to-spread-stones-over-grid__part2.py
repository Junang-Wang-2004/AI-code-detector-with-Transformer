from scipy.optimize import linear_sum_assignment as hungarian
import itertools

class C1(object):

    def minimumMoves(self, a1):
        """
        """

        def dist(a1, a2):
            return abs(a1[0] - a2[0]) + abs(a1[1] - a2[1])
        v1, v2 = ([], [])
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                if a1[v3][v4] - 1 >= 0:
                    v1.extend([(v3, v4)] * (a1[v3][v4] - 1))
                else:
                    v2.append((v3, v4))
        v5 = [[dist(v1[v3], v2[v4]) for v4 in range(len(v2))] for v3 in range(len(v1))]
        return sum((v5[v3][v4] for v3, v4 in zip(*hungarian(v5))))
