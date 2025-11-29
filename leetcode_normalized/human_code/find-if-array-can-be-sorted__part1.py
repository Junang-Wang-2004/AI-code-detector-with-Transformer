class C1(object):

    def canSortArray(self, a1):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')
        v1 = v2 = 0
        for v3 in range(len(a1)):
            if v3 + 1 != len(a1) and popcount(a1[v3 + 1]) == popcount(a1[v3]):
                continue
            if v2 > min((a1[i] for v4 in range(v1, v3 + 1))):
                return False
            v2 = max((a1[v4] for v4 in range(v1, v3 + 1)))
            v1 = v3 + 1
        return True
