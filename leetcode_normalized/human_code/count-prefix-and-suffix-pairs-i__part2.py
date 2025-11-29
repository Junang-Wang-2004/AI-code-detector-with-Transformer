class C1(object):

    def countPrefixSuffixPairs(self, a1):
        """
        """

        def check(a1, a2):
            return a1[a2].startswith(a1[a1]) and a1[a2].endswith(a1[a1])
        return sum((check(i, j) for v1 in range(len(a1)) for v2 in range(v1 + 1, len(a1))))
