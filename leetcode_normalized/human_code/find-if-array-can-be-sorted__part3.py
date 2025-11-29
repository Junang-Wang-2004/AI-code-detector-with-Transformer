class C1(object):

    def canSortArray(self, a1):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')
        v1 = 0
        for v2 in range(len(a1)):
            if v2 + 1 != len(a1) and popcount(a1[v2 + 1]) == popcount(a1[v2]):
                continue
            a1[v1:v2 + 1] = sorted(a1[v1:v2 + 1])
            v1 = v2 + 1
        return all((a1[i] <= a1[i + 1] for v3 in range(len(a1) - 1)))
