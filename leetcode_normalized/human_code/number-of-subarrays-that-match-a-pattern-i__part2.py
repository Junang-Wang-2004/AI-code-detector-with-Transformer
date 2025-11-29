class C1(object):

    def countMatchingSubarrays(self, a1, a2):
        """
        """

        def check(a1):
            return all((a1[a1 + j] == a2[j] for v1 in range(len(a2))))
        for v1 in range(len(a1) - 1):
            a1[v1] = cmp(a1[v1 + 1], a1[v1])
        return sum((check(v1) for v1 in range(len(a1) - len(a2) + 1)))
