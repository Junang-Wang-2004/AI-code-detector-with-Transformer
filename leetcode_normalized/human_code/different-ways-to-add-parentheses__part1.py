import operator
import re

class C1(object):

    def diffWaysToCompute(self, a1):
        v1 = re.split('(\\D)', a1)
        v2 = list(map(int, v1[::2]))
        v3 = list(map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, v1[1::2]))
        v4 = [[None for v5 in range(len(v2))] for v5 in range(len(v2))]

        def diffWaysToComputeRecu(a1, a2):
            if a1 == a2:
                return [v2[a1]]
            if v4[a1][a2]:
                return v4[a1][a2]
            v4[a1][a2] = [v3[i](x, y) for v1 in range(a1, a2) for v2 in diffWaysToComputeRecu(a1, v1) for v3 in diffWaysToComputeRecu(v1 + 1, a2)]
            return v4[a1][a2]
        return diffWaysToComputeRecu(0, len(v2) - 1)
