class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        v1 = 0
        v2 = float('inf')
        for v3 in range(len(a1)):
            v1 += abs(a1[v3] - a2[v3])
            if (a2[-1] - a1[v3]) * (a2[-1] - a2[v3]) <= 0:
                v2 = 0
            v2 = min(v2, abs(a2[-1] - a1[v3]), abs(a2[-1] - a2[v3]))
        v1 += 1 + v2
        return v1
