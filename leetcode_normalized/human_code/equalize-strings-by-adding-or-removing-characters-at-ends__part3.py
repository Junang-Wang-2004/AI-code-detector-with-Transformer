class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        if len(a1) < len(a2):
            a1, a2 = (a2, a1)
        v3 = 0
        v4 = [0] * (len(a2) + 1)
        for v5 in range(len(a1)):
            for v6 in reversed(range(len(a2))):
                v4[v6 + 1] = v4[v6] + 1 if a1[v5] == a2[v6] else 0
            v3 = max(v3, max(v4))
        return len(a1) + len(a2) - 2 * v3
