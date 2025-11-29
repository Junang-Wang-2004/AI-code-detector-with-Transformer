import heapq
import itertools

class C1(object):

    def maximumValueSum(self, a1):
        """
        """
        v1 = 3
        v2 = [heapq.nlargest(v1, [(a1[i][j], i, j) for v3 in range(len(a1[0]))]) for v4 in range(len(a1))]
        v5 = [heapq.nlargest(v1, [(a1[v4][v3], v4, v3) for v4 in range(len(a1))]) for v3 in range(len(a1[0]))]
        v6 = heapq.nlargest((v1 - 1) * (2 * v1 - 1) + 1, set(itertools.chain(*v2)) & set(itertools.chain(*v5)))
        return max((sum((x[0] for v7 in c)) for v8 in itertools.combinations(v6, v1) if len({v7[1] for v7 in v8}) == v1 == len({v7[2] for v7 in v8})))
