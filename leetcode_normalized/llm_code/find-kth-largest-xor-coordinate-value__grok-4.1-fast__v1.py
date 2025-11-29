class C1(object):

    def kthLargestValue(self, a1, a2):
        v1 = len(a1)
        v2 = len(a1[0])
        for v3 in range(v1):
            for v4 in range(v2):
                if v3 > 0:
                    a1[v3][v4] ^= a1[v3 - 1][v4]
                if v4 > 0:
                    a1[v3][v4] ^= a1[v3][v4 - 1]
                if v3 > 0 and v4 > 0:
                    a1[v3][v4] ^= a1[v3 - 1][v4 - 1]
        v5 = [a1[v3][v4] for v3 in range(v1) for v4 in range(v2)]
        v5.sort(reverse=True)
        return v5[a2 - 1]
