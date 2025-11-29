class C1(object):

    def subarraySum(self, a1):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2, v3 in enumerate(a1):
            v1[max(v2 - v3, 0)] += 1
            v1[v2 + 1] -= 1
        for v2 in range(len(a1)):
            v1[v2 + 1] += v1[v2]
        return sum((a1[v2] * v1[v2] for v2 in range(len(a1))))
