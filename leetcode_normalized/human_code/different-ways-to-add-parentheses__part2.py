import operator
import re

class C1(object):

    def diffWaysToCompute(self, a1):
        v1 = [[None for v2 in range(len(a1) + 1)] for v2 in range(len(a1) + 1)]
        v3 = {'+': operator.add, '-': operator.sub, '*': operator.mul}

        def diffWaysToComputeRecu(a1, a2):
            if v1[a1][a2]:
                return v1[a1][a2]
            v1 = []
            for v2 in range(a1, a2):
                if a1[v2] in v3:
                    for v3 in diffWaysToComputeRecu(a1, v2):
                        for v4 in diffWaysToComputeRecu(v2 + 1, a2):
                            v1.append(v3[a1[v2]](v3, v4))
            if not v1:
                v1 = [int(a1[a1:a2])]
            v1[a1][a2] = v1
            return v1[a1][a2]
        return diffWaysToComputeRecu(0, len(a1))
