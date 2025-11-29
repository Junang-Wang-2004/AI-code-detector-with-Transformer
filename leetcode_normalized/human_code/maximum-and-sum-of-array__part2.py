from scipy.optimize import linear_sum_assignment as hungarian
import itertools

class C1(object):

    def maximumANDSum(self, a1, a2):
        """
        """
        v1 = [[-((a1[i] if i < len(a1) else 0) & 1 + x // 2) for v2 in range(2 * a2)] for v3 in range(2 * a2)]
        return -sum((v1[v3][j] for v3, v4 in zip(*hungarian(v1))))
