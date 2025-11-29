class C1(object):

    def findPermutationDifference(self, a1, a2):
        """
        """
        v1 = [-1] * 26
        for v2, v3 in enumerate(a1):
            v1[ord(v3) - ord('a')] = v2
        return sum((abs(v1[ord(v3) - ord('a')] - v2) for v2, v3 in enumerate(a2)))
