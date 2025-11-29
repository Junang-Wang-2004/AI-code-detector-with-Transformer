class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in range(2):
            for v3 in range(v2, len(a1)):
                v4 = 0
                for v5 in range(min(len(a1) - v3, len(a2))):
                    v4 = v4 + 1 if a1[v3 + v5] == a2[v5] else 0
                    v1 = max(v1, v4)
            a1, a2 = (a2, a1)
        return len(a1) + len(a2) - 2 * v1
