class C1(object):

    def numSpecialEquivGroups(self, a1):
        """
        """

        def count(a1):
            v1 = [0] * 52
            for v2, v3 in enumerate(a1):
                v1[ord(v3) - ord('a') + 26 * (v2 % 2)] += 1
            return tuple(v1)
        return len({count(word) for v1 in a1})
