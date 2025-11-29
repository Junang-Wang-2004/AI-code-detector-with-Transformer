import heapq

class C1(object):

    def maxSum(self, a1, a2, a3):
        v1 = []
        v2 = len(a1)
        for v3 in range(v2):
            v4 = min(a3, a2[v3])
            v5 = heapq.nlargest(v4, a1[v3])
            v1.extend(v5)
        v6 = heapq.nlargest(a3, v1)
        return sum(v6)
