class C1(object):

    def numFactoredBinaryTrees(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        a1.sort()
        v2 = {}
        for v3 in range(len(a1)):
            v2[a1[v3]] = 1
            for v4 in range(v3):
                if a1[v3] % a1[v4] == 0 and a1[v3] // a1[v4] in v2:
                    v2[a1[v3]] += v2[a1[v4]] * v2[a1[v3] // a1[v4]]
                    v2[a1[v3]] %= v1
        return sum(v2.values()) % v1
