class C1(object):

    def minimumOperations(self, a1, a2):
        """
        """
        for v1 in range(len(a2)):
            a2[v1] -= a1[v1]
        return sum((max((a2[v1] if v1 < len(a2) else 0) - (a2[v1 - 1] if v1 - 1 >= 0 else 0), 0) for v1 in range(len(a2) + 1)))
