class C1(object):

    def minimumOperations(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1) - 1):
            for v3 in range(len(a1[0])):
                if a1[v2][v3] + 1 <= a1[v2 + 1][v3]:
                    continue
                v1 += a1[v2][v3] + 1 - a1[v2 + 1][v3]
                a1[v2 + 1][v3] = a1[v2][v3] + 1
        return v1
