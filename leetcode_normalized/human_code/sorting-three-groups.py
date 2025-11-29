class C1(object):

    def minimumOperations(self, a1):
        """
        """
        v1 = 3
        v2 = [0] * v1
        for v3 in a1:
            v2[v3 - 1] += 1
            for v4 in range(v3, len(v2)):
                v2[v4] = max(v2[v4], v2[v4 - 1])
        return len(a1) - v2[-1]
