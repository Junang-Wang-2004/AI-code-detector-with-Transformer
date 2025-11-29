import heapq

class C1(object):

    def minFallingPathSum(self, a1):
        """
        """
        for v1 in range(1, len(a1)):
            v2 = heapq.nsmallest(2, a1[v1 - 1])
            for v3 in range(len(a1[0])):
                a1[v1][v3] += v2[1] if a1[v1 - 1][v3] == v2[0] else v2[0]
        return min(a1[-1])
