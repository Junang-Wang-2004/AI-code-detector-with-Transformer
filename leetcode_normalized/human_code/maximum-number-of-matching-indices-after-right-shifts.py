class C1(object):

    def maximumMatchingIndices(self, a1, a2):
        """
        """
        return max((sum((a2[j] == a1[(i + j) % len(a1)] for v1 in range(len(a2)))) for v2 in range(len(a1))))
