class C1(object):

    def distinctNames(self, a1):
        """
        """
        v1 = [set() for v2 in range(26)]
        for v3 in a1:
            v1[ord(v3[0]) - ord('a')].add(v3[1:])
        v4 = 0
        for v5 in range(len(v1)):
            for v6 in range(v5 + 1, len(v1)):
                v7 = len(v1[v5] & v1[v6])
                v4 += (len(v1[v5]) - v7) * (len(v1[v6]) - v7)
        return v4 * 2
